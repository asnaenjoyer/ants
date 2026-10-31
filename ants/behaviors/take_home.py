from .behavior import Behavior
from .timer import Timer
import random
import pygame.math

class TakeHome(Behavior):
    def __init__(self, ant, nest) -> None:
        super().__init__(ant)
        self.nest = nest

    def on_start(self):
        print("Taking Home")

    def update(self, delta_time: float):
        direction = self.nest.position - self.ant.position
        self.ant.set_direction(direction)
        self.ant.move(delta_time)
            
