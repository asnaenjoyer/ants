from ants.states.ant_state import AntState
from ants.pheromones.pheromone_type import PheromoneType

class Returning(AntState):
    def __init__(self, ant):
            super().__init__(ant)
            self.pheromone_type = PheromoneType.RED
            self.target_pheromone_type = PheromoneType.BLUE
            print("Ant is now returning to the nest.")

    def update(self, delta_time: float) -> None:
        direction = self.ant.nest.position - self.ant.position

        if direction.length() < 10:
            self.ant.set_searching()
            self.ant.carrying_food = False
            return

        self.ant.direction = direction.normalize()