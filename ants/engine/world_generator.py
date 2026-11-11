import random
import pygame

from ants.engine import world
from ants.entities.ant import Ant
from ants.entities.food import Food
from ants.entities.nest import Nest


class WorldGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate(self, world):
        self._generate_food(world)
        world.nest = Nest(self.settings.world_width // 2, self.settings.world_height // 2, self.settings.unit_size)
        world.ants.add(Ant(world.food, world.nest,
                           pygame.Vector2(self.settings.world_width // 2, self.settings.world_height // 2), 
                           self.settings.unit_size))

    def _generate_food(self, world):
        max_x = max(0, self.settings.world_width - 1)
        max_y = max(0, self.settings.world_height - 1)

        for _ in range(52):
            x = random.randint(32, max_x - 32)
            y = random.randint(32, max_y - 32)
            food = Food(x, y, self.settings.unit_size)
            world.food.add(food)