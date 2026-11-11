from ants.states.ant_state import AntState
from ants.states.returning import Returning
from ants.pheromones.pheromone_type import PheromoneType

class Searching(AntState):
    def __init__(self, ant):
        super().__init__(ant)
        self.pheromone_type = PheromoneType.BLUE
        self.target_pheromone_type = PheromoneType.RED
        print("Ant is now searching for food.")

    def update(self, delta_time: float) -> None:
        self.check_for_food()
        self.ant.random_walk.update(self.ant.direction, delta_time)

    def check_for_food(self) -> None:
        for food in self.ant.food_group:
            if self.ant.rect.colliderect(food.hitbox):
                food.kill()
                self.ant.carrying_food = True
                self.ant.set_returning()
                return