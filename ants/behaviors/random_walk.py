
import random
import pygame


class RandomWalk:
    def __init__(self, min_interval: float = 1.0, max_interval: float = 3.0, turn_speed: float = 120.0) -> None:
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.turn_speed = turn_speed

        self.timer = 0.0
        self.target_direction = pygame.Vector2(1, 0)

    def choose_direction(self) -> None:
        angle = random.uniform(0, 360)
        self.target_direction = pygame.Vector2(1, 0).rotate(angle)
        self.timer = random.uniform(self.min_interval, self.max_interval)

    def update(self, direction: pygame.Vector2, delta_time: float) -> pygame.Vector2:
        self.timer -= delta_time

        if self.timer <= 0:
            self.choose_direction()

        angle = direction.angle_to(self.target_direction)
        max_rotation = self.turn_speed * delta_time

        rotation = max(-max_rotation, min(angle, max_rotation))
        direction.rotate_ip(rotation)

        return direction
