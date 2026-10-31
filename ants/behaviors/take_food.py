from .behavior import Behavior
from .take_home import TakeHome
from .timer import Timer
import random
import pygame.math

class TakeFood(Behavior):
    def __init__(self, ant, found) -> None:
        super().__init__(ant)
        self.found = found
        self.timer = Timer(1)

    def on_start(self):
        self.timer = Timer(random.randrange(1, 10))
        print("Taking Food")

    def update(self, delta_time: float):
        if self.timer.tick(delta_time):
            free_space = self.ant.max_amount - self.ant.amount
            self.ant.amount += self.found.take(free_space)
            self.ant.set_behavior(TakeHome(self.ant, self.ant.nest.sprite))
