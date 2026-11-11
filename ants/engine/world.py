import pygame
from ants.entities.food import Food
from ants.entities.nest import Nest
from ants.settings import Settings
from ants.pheromones.pheromone_field import PheromoneField


class World:
    def __init__(self, settings: Settings) -> None:
        self.food = pygame.sprite.Group()
        self.nest : None | Nest = None
        self.ants = pygame.sprite.Group()

        self.pheromone_field = PheromoneField((settings.world_width, settings.world_height), settings.pheromone_cell_size, settings.max_pheromone_concentration, settings.pheromone_evaporation_rate)

        self.background = pygame.Surface((settings.world_width, settings.world_height))
        self.background.fill(settings.background_color)

    def update(self, delta_time: float) -> None:
        self.food.update(delta_time)
        self.ants.update(delta_time)
        self.pheromone_field.evaporate(delta_time)
        if self.nest:
            self.nest.update(delta_time)
