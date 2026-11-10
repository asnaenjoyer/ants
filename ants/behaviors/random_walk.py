import random
from math import cos, radians, sin

from .behavior import Behavior
from .timer import Timer
from ants.vector import Vector2


class RandomWalk(Behavior):
    def __init__(self, ant) -> None:
        super().__init__(ant)
        self.walk_timer = Timer(random.randrange(1, 3))

    def on_start(self):
        pass

    def update(self, delta_time: float):
        if self.ant.amount > 0:
            self.ant.behavior_manager.change("take_home", nest=self.ant.memory["nest"])
            return

        if (self.walk_timer.tick(delta_time)):
            angle = random.uniform(0, 360)
            angle_radians = radians(angle)
            direction = Vector2(cos(angle_radians), sin(angle_radians))
            self.ant.set_direction(direction)
            self.walk_timer.set_interval(random.randrange(1, 3))
        self.ant.move(delta_time)

        found = self.ant.check_food(self.ant.food_group)
        if found is not None and found.amount > 0:
            self.ant.memory["food"] = found
            self.ant.behavior_manager.change("food_find", found=found)