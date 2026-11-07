import pygame

from ants.managers import BehaviorManager
from ants.behaviors.behavior import Behavior
from ants.settings import Settings


class Ant(pygame.sprite.Sprite):
    COLOR = (75, 45, 35)

    def __init__(self, settings: Settings, food_group: pygame.sprite.Group, nest: pygame.sprite.GroupSingle) -> None:
        super().__init__()
        self.settings = settings

        self.food_group = food_group

        self.original_image = pygame.Surface((48, 32), pygame.SRCALPHA)
        self.image = self.original_image.copy()
        pygame.draw.ellipse(self.original_image, self.COLOR, (4, 9, 18, 14))
        pygame.draw.ellipse(self.original_image, self.COLOR, (19, 11, 12, 10))
        pygame.draw.circle(self.original_image, self.COLOR, (36, 16), 6)

        self.rect = self.image.get_rect(
            center=(settings.window_width // 2, settings.window_height // 2)
        )

        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)
        
        self.look_angle: float = 0
        self.direction = pygame.Vector2(0, 0)

        self.speed = 100

        self.detection_radius = 150
        self.max_amount = 25
        self.amount = 0

        self.memory = {"food": None, "nest": nest.sprite}

        self.behavior_manager : BehaviorManager = BehaviorManager(self) 
        self.behavior_manager.change("random_walk")
        self.rotate()

    def check_food(self, food_group: pygame.sprite.Group):
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

    def _check_borders(self):
        if self.position.x - self.rect.width // 2 <= 0 and self.direction.x < 0:
            self.direction.x *= -1
            self.rotate()
        elif self.position.x + self.rect.width // 2 >= self.settings.window_width and self.direction.x > 0:
            self.direction.x *= -1
            self.rotate()
        if self.position.y - self.rect.height // 2 <= 0 and self.direction.y < 0:
            self.direction.y *= -1
            self.rotate()
        elif self.position.y + self.rect.height // 2 >= self.settings.window_height and self.direction.y > 0:
            self.direction.y *= -1
            self.rotate()

    def set_direction(self, direction):
        self.direction = direction
        self.rotate()

    def move(self, delta_time):
        if self.direction.length_squared() > 0:
            self.direction.normalize_ip()

        self._check_borders()

        half_width = self.rect.width // 2
        half_height = self.rect.height // 2

        self.position += self.direction * self.speed * delta_time
        
        self.position.x = max(half_width, min(self.position.x, self.settings.window_width - half_width))
        self.position.y = max(half_height, min(self.position.y, self.settings.window_height - half_height))

        self.rect.center = (round(self.position.x), round(self.position.y))

    def rotate(self):
        self.look_angle = -self.direction.as_polar()[1]

        center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, self.look_angle)
        self.rect = self.image.get_rect(center=center)

    def update_memory(self):
        if self.memory["food"] is not None and self.memory["food"] not in self.food_group:
            self.memory["food"] = None

    def update(self, delta_time):
        self.behavior_manager.update(delta_time)
        self.memory.update()