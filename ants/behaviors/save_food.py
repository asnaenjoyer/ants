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

    def update(self, delta_time: float):
        if not self.timer.tick(delta_time):
            return

        if self.ant.amount > 0:
            deposited = self.nest.deposit(self.ant.amount)
            self.ant.amount -= deposited

        self.ant.memory["food"] = None
        if self.ant.amount > 0:
            self.ant.behavior_manager.change("take_home", nest=self.ant.memory["nest"])
        else:
            self.ant.behavior_manager.change("random_walk")