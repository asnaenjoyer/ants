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

        x = random.randint(0, self.settings.world_width)
        y = random.randint(0, self.settings.world_height)

        nest = Nest(x, y)
        colony.add_nest(nest)

        for _ in range(self.settings.num_ants):
            ant = Ant(self.settings, food, nest, pygame.Vector2(nest.rect.center))
            colony.add_ant(ant)

        return colony

    def _generate_food(self, world):
        for _ in range(self.settings.num_food):
            x = random.randint(0, self.settings.world_width)
            y = random.randint(0, self.settings.world_height)
            food = Food(x, y, 50)
            world.food.add(food)