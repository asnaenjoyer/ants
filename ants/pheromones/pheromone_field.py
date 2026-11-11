import numpy as np
import pygame

from ants.pheromones.pheromone_type import PheromoneType


class PheromoneField:
    def __init__(self, world_size: tuple[int, int], cell_size: int = 10, 
                 max_concentration: float = 100.0, evaporation_rate: float = 2.0) -> None:
        self.cell_size = cell_size
        self.max_concentration = max_concentration
        self.evaporation_rate = evaporation_rate

        width, height = world_size

        self.columns = (width + cell_size - 1) // cell_size
        self.rows = (height + cell_size - 1) // cell_size

        shape = (self.rows, self.columns)

        self.grids = {
            PheromoneType.RED: np.zeros(shape, dtype=np.float32),
            PheromoneType.BLUE: np.zeros(shape, dtype=np.float32)
        }

    def _get_cell(self, position: pygame.Vector2) -> tuple[int, int]:
        column = int(position.x // self.cell_size)
        row = int(position.y // self.cell_size)

        return row, column

    def deposit(self, position: pygame.Vector2, pheromone_type: PheromoneType, amount: float) -> None:
        row, column = self._get_cell(position)

        if not (0 <= row < self.rows and 0 <= column < self.columns):
            return

        grid = self.grids[pheromone_type]
        grid[row, column] = min(grid[row, column] + amount, self.max_concentration)

    def get_concentration(self, position: pygame.Vector2, pheromone_type: PheromoneType) -> float:
        row, column = self._get_cell(position)

        if not (0 <= row < self.rows and 0 <= column < self.columns):
            return 0.0

        return float(self.grids[pheromone_type][row, column])

    def get_average_concentration(self, position, radius, pheromone_type):
        grid = self.grids[pheromone_type]

        min_column = max(0, int((position.x - radius) // self.cell_size))
        max_column = min(self.columns - 1, int((position.x + radius) // self.cell_size))
        min_row = max(0, int((position.y - radius) // self.cell_size))
        max_row = min(self.rows - 1, int((position.y + radius) // self.cell_size))

        values = []

        for row in range(min_row, max_row + 1):
            for column in range(min_column, max_column + 1):
                cell_position = pygame.Vector2(
                    (column + 0.5) * self.cell_size,
                    (row + 0.5) * self.cell_size
                )

                if cell_position.distance_to(position) <= radius:
                    values.append(grid[row, column])

        if not values:
            return 0.0

        return float(sum(values) / len(values))

    def evaporate(self, delta_time: float) -> None:
        for grid in self.grids.values():
            grid -= self.evaporation_rate * delta_time
            np.maximum(grid, 0, out=grid)
