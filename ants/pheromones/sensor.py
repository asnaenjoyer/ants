import pygame

from ants.pheromones.pheromone_field import PheromoneField
from ants.pheromones.pheromone_type import PheromoneType

class Sensor:
    def __init__(self, angle: float, distance: float = 30, radius: float = 10):
        self.angle = angle
        self.distance = distance
        self.radius = radius

        self.position = pygame.Vector2()
        self.concentration = 0.0

    def update(self, ant_position, direction, field: PheromoneField, pheromone_type: PheromoneType):
        sensor_direction = direction.rotate(self.angle)
        self.position = ant_position + sensor_direction * self.distance

        self.concentration = field.get_average_concentration(
            self.position,
            self.radius,
            pheromone_type
        )