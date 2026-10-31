from .behavior import Behavior
from .food_find import FoodFind
from .timer import Timer
import random
import pygame.math

class RandomWalk(Behavior):
    def __init__(self, ant) -> None:
        super().__init__(ant)
        
        self.walk_timer = Timer(random.randrange(1, 3))
    

    def on_start(self):
        print("Random Walk")

    def check_food(self, food):
        closest_food = None
        min_distance = float("inf")

        for f in food:
            distance = self.ant.position.distance_to(f.position)

            if distance < min_distance:
                min_distance = distance
                closest_food = f

        if min_distance <= self.ant.detection_radius:
            return closest_food
        else:
            return None

    def update(self, delta_time: float):
        if (self.walk_timer.tick(delta_time)):
            angle = random.uniform(0, 360)
            direction = pygame.Vector2(1, 0).rotate(angle)
            self.ant.set_direction(direction)
            self.walk_timer.set_interval(random.randrange(1, 3))
        self.ant.move(delta_time)

        found = self.check_food(self.ant.food)
        if found is not None:
            self.ant.set_behavior(FoodFind(self.ant, found))