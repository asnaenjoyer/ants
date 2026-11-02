from .behavior import Behavior


class FoodFind(Behavior):
    def __init__(self, ant, found) -> None:
        super().__init__(ant)
        self.found = found

    def on_start(self):
        print("Found Food")

    def update(self, delta_time: float):
        if self.found not in self.ant.food:
            self.ant.behavior_manager.change("random_walk")
            return
        
        direction = self.found.position - self.ant.position
        self.ant.set_direction(direction)
        if self.ant.position.distance_to(self.found.position) > 16:
            self.ant.move(delta_time)
        else:
            self.ant.behavior_manager.change("take_food", found=self.found)
