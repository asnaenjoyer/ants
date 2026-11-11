
import random
import pygame

from ants.entities.ant import Ant
from ants.entities.food import Food
from ants.entities.nest import Nest


class WorldGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate(self, world):
        self._generate_food(world)
        world.nest = Nest(
            self.settings.world_width // 2,
            self.settings.world_height // 2,
            self.settings.unit_size
        )

        world.ants.add(Ant(
            world.food,
            world.nest,
            pygame.Vector2(self.settings.world_width // 2, self.settings.world_height // 2),
            world.pheromone_field,
            self.settings
        ))

    def _generate_food(self, world):
        margin = 32
        cluster_count = 5
        cluster_radius = 70

        for _ in range(cluster_count):
            center_x = random.randint(margin, self.settings.world_width - margin)
            center_y = random.randint(margin, self.settings.world_height - margin)

            food_count = random.randint(8, 14)

            for _ in range(food_count):
                x = int(random.gauss(center_x, cluster_radius / 2))
                y = int(random.gauss(center_y, cluster_radius / 2))

                x = max(margin, min(x, self.settings.world_width - margin))
                y = max(margin, min(y, self.settings.world_height - margin))

                world.food.add(Food(x, y, self.settings.unit_size))
