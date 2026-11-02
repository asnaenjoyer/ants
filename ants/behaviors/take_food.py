import random

from .behavior import Behavior
from .timer import Timer


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
            taken = self.found.take(free_space)
            if taken == 0:
                self.ant.behavior_manager.change("random_walk")
                return

            self.ant.amount += taken
            self.ant.behavior_manager.change("take_home", nest=self.ant.nest.sprite)
