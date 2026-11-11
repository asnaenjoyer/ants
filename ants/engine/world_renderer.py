import pygame

from .camera import Camera
from .world import World
from ants.pheromones.pheromone_type import PheromoneType


class WorldRenderer:
    def __init__(self, screen: pygame.Surface, camera: Camera, background_color) -> None:
        self.screen = screen
        self.camera = camera
        self.background_color = background_color

    
    def draw_pheromone_grid(self, world, pheromone_type, color):
        field = world.pheromone_field
        grid = field.grids[pheromone_type]

        surface = pygame.Surface((field.columns * field.cell_size, field.rows * field.cell_size), pygame.SRCALPHA)

        for row in range(field.rows):
            for column in range(field.columns):
                concentration = grid[row, column]

                if concentration <= 0:
                    continue

                alpha = int(255 * concentration / field.max_concentration)

                pygame.draw.rect(surface, (*color, alpha),
                    (
                        column * field.cell_size,
                        row * field.cell_size,
                        field.cell_size,
                        field.cell_size
                    )
                )

        self.camera.draw_surface(surface, (0, 0), self.screen)


    def draw_pheromones(self, world):
        self.draw_pheromone_grid(world, PheromoneType.RED, (255, 40, 40))
        self.draw_pheromone_grid(world, PheromoneType.BLUE, (40, 100, 255))

    def draw_sensors(self, world):
        for ant in world.ants:
            for sensor in ant.sensors:
                concentration = sensor.concentration
                intensity = min(1.0, concentration / world.pheromone_field.max_concentration)

                base_color = (
                    (255, 40, 40)
                    if ant.state.target_pheromone_type == PheromoneType.RED
                    else (40, 100, 255)
                )

                color = tuple(
                    int(60 + (channel - 60) * intensity)
                    for channel in base_color
                )

                radius = max(2, int(sensor.radius * self.camera.zoom))
                position = self.camera.apply(
                    pygame.Rect(sensor.position.x, sensor.position.y, 0, 0)
                ).topleft

                pygame.draw.circle(self.screen, color, position, radius)
                pygame.draw.circle(self.screen, (255, 255, 255), position, radius, 1)
        

    def draw(self, world: World) -> None:
        background_rect = self.camera.apply(world.background.get_rect())
        self.screen.fill(self.background_color, background_rect)

        self.draw_pheromones(world)
        self.draw_sensors(world)
        self.camera.draw_group(world.food, self.screen)

        if world.nest:
            self.camera.draw_sprite(world.nest, self.screen)

        self.camera.draw_group(world.ants, self.screen)