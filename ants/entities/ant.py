import pygame

from ants.entities.nest import Nest
from ants.behaviors.random_walk import RandomWalk
from ants.pheromones.pheromone_field import PheromoneField
from ants.pheromones.sensor import Sensor
from ants.settings import Settings
from ants.states.ant_state import AntState
from ants.states.searching import Searching


class Ant(pygame.sprite.Sprite):
    COLOR = (75, 45, 35)

    def __init__(self, food_group: pygame.sprite.Group, nest: Nest, pos: pygame.Vector2, pheromone_field : PheromoneField, settings : Settings) -> None:
        super().__init__()
        self.settings = settings

        self.image = pygame.Surface((settings.unit_size * 3, settings.unit_size + 2), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.COLOR, (0, 0, settings.unit_size + 1, settings.unit_size+1))
        pygame.draw.ellipse(self.image, self.COLOR, (settings.unit_size, 0, settings.unit_size, settings.unit_size))
        pygame.draw.ellipse(self.image, self.COLOR, (settings.unit_size * 2, 0, settings.unit_size, settings.unit_size))
        self.original_image = self.image.copy() 

        self.rect = self.image.get_rect(center=(pos.x, pos.y))
        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)
        self.direction: pygame.Vector2 = pygame.Vector2(-0.5, 0.5)
        self.speed: float = 100.0

        self.food_group = food_group
        self.nest = nest

        self.random_walk = RandomWalk(min_interval=1.0, max_interval=3.0, turn_speed=100.0)

        self.state: AntState = Searching(self)
        self.carrying_food = False

        self.pheromone_field = pheromone_field
        self.last_pheromone_position = pygame.Vector2(pos)
        self.sensors = [
            Sensor(-45, distance=40, radius=16),
            Sensor(0, distance=40, radius=16),
            Sensor(45, distance=40, radius=16)
        ]


    def change_state(self, state: AntState) -> None:
        self.state = state

    def set_searching(self) -> None:
        from ants.states.searching import Searching
        self.change_state(Searching(self))

    def set_returning(self) -> None:
        from ants.states.returning import Returning
        self.change_state(Returning(self))

    def _check_bounds(self) -> None:
        if self.position.x < 0:
            self.position.x = 0
            self.direction.x *= -1
        elif self.position.x > self.settings.world_width:
            self.position.x = self.settings.world_width
            self.direction.x *= -1

        if self.position.y < 0:
            self.position.y = 0
            self.direction.y *= -1
        elif self.position.y > self.settings.world_height:
            self.position.y = self.settings.world_height
            self.direction.y *= -1


    def move(self, delta_time: float) -> None:
        self._check_bounds()
        self.position += self.direction * self.speed * delta_time
        self.rect.center = (int(self.position.x), int(self.position.y))

    def emit_pheromone(self) -> None:
        distance = self.position.distance_to(self.last_pheromone_position)

        if distance < 8:
            return

        self.pheromone_field.deposit(self.position, self.state.pheromone_type, self.settings.pheromone_deposit_amount)

        self.last_pheromone_position = self.position.copy()

    def update_image(self) -> None:
        angle = pygame.Vector2(1, 0).angle_to(self.direction)
        self.image = pygame.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.carrying_food:
            pygame.draw.circle(self.image, (200, 45, 35), self.image.get_rect().center, 4)

    def update_sensors(self):
        for sensor in self.sensors:
            sensor.update(self.position, self.direction, self.pheromone_field, self.state.target_pheromone_type)

    def update(self, delta_time: float) -> None: 
        self.state.update(delta_time)
        self.move(delta_time)
        self.update_sensors()
        self.emit_pheromone()
        self.update_image()
