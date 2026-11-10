from ants.entities.nest import Nest
from ants.entities.ant import Ant
import pygame

class Colony:
    def __init__(self):
        self.ants = pygame.sprite.Group()
        self.nest : Nest | None = None

    def add_ant(self, ant: Ant):
        self.ants.add(ant)

    def add_nest(self, nest: Nest):
        self.nest = nest

    def update(self, delta_time: float) -> None:
        self.ants.update(delta_time)
        if self.nest:
            self.nest.update(delta_time)