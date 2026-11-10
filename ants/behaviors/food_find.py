from .behavior import Behavior


class FoodFind(Behavior):
    def __init__(self, ant, found) -> None:
        super().__init__(ant)
        self.found = found

    def on_start(self):
        pass

    def update(self, delta_time: float):
        if self.ant.amount > 0:
            self.ant.behavior_manager.change("take_home", nest=self.ant.memory["nest"])
            return

        if self.found not in self.ant.food_group or self.found.amount <= 0:
            self.ant.memory["food"] = None
            self.ant.behavior_manager.change("random_walk")
            return

        direction = self.found.position - self.ant.position
        self.ant.set_direction(direction)
        if self.ant.position.distance_to(self.found.position) > 16:
            self.ant.move(delta_time)
        else:
            self.ant.memory["food"] = self.found
            self.ant.behavior_manager.change("take_food", found=self.found)
