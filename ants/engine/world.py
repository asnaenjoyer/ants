import pygame
from ants.entities.food import Food
from ants.settings import Settings
from ants.colony.colony import Colony


class World:
    def __init__(self, settings: Settings) -> None:
        self.food = pygame.sprite.Group()
        self.colonies: list[Colony] = []
        self.background = pygame.Surface((settings.world_width, settings.world_height))
        self.background.fill(settings.background_color)

    def update(self, delta_time: float) -> None:
        for colony in self.colonies:
            colony.update(delta_time)
        self.food.update()
