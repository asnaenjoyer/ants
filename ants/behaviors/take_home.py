from .behavior import Behavior


class TakeHome(Behavior):
    def __init__(self, ant, nest=None) -> None:
        super().__init__(ant)
        self.nest = nest if nest is not None else self.ant.memory["nest"]

    def on_start(self):
        print("Taking Home")

    def update(self, delta_time: float):
        if self.nest is None:
            return

        direction = self.nest.position - self.ant.position
        self.ant.set_direction(direction)
        if self.ant.position.distance_to(self.nest.position) > 16:
            self.ant.move(delta_time)
        else:
            self.ant.behavior_manager.change("save_food", nest=self.nest)

