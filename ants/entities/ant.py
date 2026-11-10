from math import atan2, ceil, cos, degrees, radians, sin

from ants.entities.food import Food
from ants.entities.nest import Nest
from ants.managers import BehaviorManager
from ants.settings import Settings
from ants.vector import Vector2


class Ant:
    WIDTH = 48
    HEIGHT = 32

    def __init__(self, settings: Settings, food_group: list[Food], nest: Nest, pos: Vector2) -> None:
        self.settings = settings
        self.food_group = food_group

        self.position = Vector2(pos.x, pos.y)
        self.look_angle: float = 0
        self.direction = Vector2()

        self.speed = 100

        self.detection_radius = 150
        self.max_amount = 5
        self.amount = 0

        self.memory = {"food": None, "nest": nest}

        self.behavior_manager: BehaviorManager = BehaviorManager(self)
        self.behavior_manager.change("random_walk")

    def check_food(self, food_group: list[Food]) -> Food | None:
        closest_food = None
        min_distance = float("inf")

        for food in food_group:
            distance = self.position.distance_to(food.position)

            if distance < min_distance:
                min_distance = distance
                closest_food = food

        if min_distance <= self.detection_radius:
            return closest_food

        return None

    def _half_size(self) -> tuple[float, float]:
        angle = radians(self.look_angle)
        half_width = ceil(abs(cos(angle)) * self.WIDTH / 2 + abs(sin(angle)) * self.HEIGHT / 2)
        half_height = ceil(abs(sin(angle)) * self.WIDTH / 2 + abs(cos(angle)) * self.HEIGHT / 2)
        return half_width, half_height

    def _check_borders(self):
        half_width, half_height = self._half_size()
        if self.position.x - half_width <= 0 and self.direction.x < 0:
            self.direction.x *= -1
            self.rotate()
        elif self.position.x + half_width >= self.settings.world_width and self.direction.x > 0:
            self.direction.x *= -1
            self.rotate()
        if self.position.y - half_height <= 0 and self.direction.y < 0:
            self.direction.y *= -1
            self.rotate()
        elif self.position.y + half_height >= self.settings.world_height and self.direction.y > 0:
            self.direction.y *= -1
            self.rotate()

    def set_direction(self, direction: Vector2) -> None:
        self.direction = Vector2(direction.x, direction.y)
        self.rotate()

    def move(self, delta_time: float) -> None:
        if self.direction.length_squared() > 0:
            self.direction.normalize_ip()

        self._check_borders()

        half_width, half_height = self._half_size()

        self.position += self.direction * self.speed * delta_time
        
        self.position.x = max(half_width, min(self.position.x, self.settings.world_width - half_width))
        self.position.y = max(half_height, min(self.position.y, self.settings.world_height - half_height))

    def rotate(self) -> None:
        if self.direction.length_squared() > 0:
            self.look_angle = -degrees(atan2(self.direction.y, self.direction.x))
        else:
            self.look_angle = 0

    def update_memory(self) -> None:
        if self.memory["food"] is not None and self.memory["food"] not in self.food_group:
            self.memory["food"] = None

    def update(self, delta_time: float) -> None:
        self.update_memory()
        self.behavior_manager.update(delta_time)