import random
import pygame

from ants.colony.colony import Colony
from ants.engine import world
from ants.entities.ant import Ant
from ants.entities.food import Food
from ants.entities.nest import Nest


class WorldGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate(self, world):
        colony = self._generate_colony(world.food)
        world.colonies.append(colony)
        self._generate_food(world)

    def _generate_colony(self, food: pygame.sprite.Group) -> Colony:
        colony = Colony()

        max_x = max(0, self.settings.world_width - 1)
        max_y = max(0, self.settings.world_height - 1)

        x = random.randint(0, max_x)
        y = random.randint(0, max_y)

        nest = Nest(x, y, self.settings.nest_max_amount)
        colony.add_nest(nest)

        for _ in range(self.settings.num_ants):
            offset = pygame.Vector2(
                random.uniform(-25, 25),
                random.uniform(-25, 25),
            )
            spawn_position = pygame.Vector2(nest.rect.center) + offset
            ant = Ant(self.settings, food, nest, spawn_position)
            colony.add_ant(ant)

        return colony

    def _generate_food(self, world):
        max_x = max(0, self.settings.world_width - 1)
        max_y = max(0, self.settings.world_height - 1)

        for _ in range(self.settings.num_food):
            x = random.randint(32, max_x - 32)
            y = random.randint(32, max_y - 32)
            food = Food(x, y, self.settings.food_amount)
            world.food.add(food)