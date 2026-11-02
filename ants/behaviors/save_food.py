import random

from .behavior import Behavior
from .timer import Timer


class SaveFood(Behavior):
    def __init__(self, ant, nest=None) -> None:
        super().__init__(ant)
        self.nest = nest if nest is not None else self.ant.nest.sprite
        self.timer = Timer(1)

    def on_start(self):
        self.timer = Timer(random.randrange(1, 5))
        print("Saving Food")

    def update(self, delta_time: float):
        if self.timer.tick(delta_time):
            if self.ant.amount > 0:
                deposited = self.nest.deposit(self.ant.amount)
                self.ant.amount -= deposited
                print(f"Deposited {deposited} food. Ant now has {self.ant.amount} food.")
            else:
                print("No food to deposit.")
            self.ant.behavior_manager.change("random_walk")

