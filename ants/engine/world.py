import pygame
from ants.entities.ant import Ant
from ants.entities.food import Food
from ants.entities.nest import Nest
from ants.settings import Settings



class World:
    def __init__(self, settings: Settings) -> None:
        self.food = pygame.sprite.Group()
        self.nest = pygame.sprite.GroupSingle()
        self.ants = pygame.sprite.Group()
        self.background = pygame.Surface((settings.world_width, settings.world_height))
        self.background.fill(settings.background_color)

    def update(self, delta_time: float) -> None:
        self.ants.update(delta_time)
        self.food.update()
        self.nest.update()