import random

from .behavior import Behavior
from .timer import Timer


class SaveFood(Behavior):
    def __init__(self, ant, nest=None) -> None:
        super().__init__(ant)
        self.nest = nest if nest is not None else self.ant.memory["nest"]
        self.timer = Timer(1)

    def on_start(self):
        self.timer = Timer(random.randrange(1, 5))
        print("Saving Food")

    def update(self, delta_time: float):
        if not self.timer.tick(delta_time):
            return

        if self.ant.amount > 0:
            deposited = self.nest.deposit(self.ant.amount)
            self.ant.amount -= deposited
            print(f"Deposited {deposited} food. Ant now has {self.ant.amount} food.")

        if self.ant.memory["food"] is not None:
            self.ant.behavior_manager.change("food_find", found=self.ant.memory["food"])
        else:
            self.ant.behavior_manager.change("random_walk")