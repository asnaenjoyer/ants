from .behavior import Behavior
from .take_food import TakeFood
from .timer import Timer
import random
import pygame.math

class FoodFind(Behavior):
    def __init__(self, ant, found) -> None:
        super().__init__(ant)
        self.found = found

    def on_start(self):
        print("Found Food")

    def update(self, delta_time: float):
        direction = self.found.position - self.ant.position
        self.ant.set_direction(direction)
        if (self.ant.position.distance_to(self.found.position) > 16):
            self.ant.move(delta_time)
        else:
            self.ant.set_behavior(TakeFood(self.ant, self.found))