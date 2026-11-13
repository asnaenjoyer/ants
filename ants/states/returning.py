from ants.states.ant_state import AntState
from ants.pheromones.pheromone_type import PheromoneType


class Returning(AntState):
    def __init__(self, ant):
        super().__init__(ant)
        self.pheromone_type = PheromoneType.RED
        self.target_pheromone_type = PheromoneType.BLUE

        direction = self.ant.nest.position - self.ant.position
        self.ant.direction = direction.normalize()


    def update(self, delta_time: float) -> None:
        to_nest = self.ant.nest.position - self.ant.position

        if to_nest.length() < 10:
            self.ant.set_searching()
            self.ant.carrying_food = False
            return

        if not self.ant.follow_pheromone(delta_time):
            self.ant.direction = to_nest.normalize()
            return

        if self.ant.direction.dot(to_nest) <= 0:
            self.ant.direction = to_nest.normalize()