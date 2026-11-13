from ants.states.ant_state import AntState
from ants.states.returning import Returning
from ants.pheromones.pheromone_type import PheromoneType

class Searching(AntState):
    def __init__(self, ant):
        super().__init__(ant)
        self.pheromone_type = PheromoneType.BLUE
        self.target_pheromone_type = PheromoneType.RED

    def update(self, delta_time: float) -> None:
        food = self.find_food()

        if food:
            direction = food.position - self.ant.position

            if direction.length() > 0:
                self.ant.direction = direction.normalize()
        else:
            self.ant.random_walk.update(self.ant.direction, delta_time)

        self.check_for_food()


    def find_food(self):
        closest_food = None
        min_distance = self.ant.settings.food_detection_radius

        for food in self.ant.food_group:
            distance = self.ant.position.distance_to(food.position)

            if distance < min_distance:
                min_distance = distance
                closest_food = food

        return closest_food


    def check_for_food(self) -> None:
        for food in self.ant.food_group:
            if self.ant.rect.colliderect(food.hitbox):
                food.kill()
                self.ant.carrying_food = True
                self.ant.set_returning()
                return