import pygame
from ants.entities.ant import Ant
from ants.entities.food import Food
from ants.entities.nest import Nest
from ants.settings import Settings



class World:
    def __init__(self, settings: Settings) -> None:
        self.food = pygame.sprite.Group()
        self.food.add(Food(200, 150, 50))
        self.nest = pygame.sprite.GroupSingle()
        self.nest.add(Nest(400, 300))
        self.ants = pygame.sprite.Group()
        self.ants.add(Ant(settings, self.food, self.nest))
        for _ in range(2):
            self.ants.add(Ant(settings, self.food, self.nest))

    def update(self, delta_time: float) -> None:
        self.ants.update(delta_time)
        self.food.update()
        self.nest.update()