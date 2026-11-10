import pygame

from .camera import Camera
from .world import World


class WorldRenderer:
    ANT_COLOR = (75, 45, 35)
    FOOD_COLOR = (200, 45, 35)
    NEST_COLOR = (35, 35, 20)

    def __init__(self, screen: pygame.Surface, camera: Camera, background_color) -> None:
        self.screen = screen
        self.camera = camera
        self.background_color = background_color
        self._ant_image = pygame.Surface((48, 32), pygame.SRCALPHA)
        pygame.draw.ellipse(self._ant_image, self.ANT_COLOR, (4, 9, 18, 14))
        pygame.draw.ellipse(self._ant_image, self.ANT_COLOR, (19, 11, 12, 10))
        pygame.draw.circle(self._ant_image, self.ANT_COLOR, (36, 16), 6)
        self._food_image = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.ellipse(self._food_image, self.FOOD_COLOR, (0, 0, 16, 16))
        self._nest_image = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.ellipse(self._nest_image, self.NEST_COLOR, (0, 0, 16, 16))

    def draw(self, world: World) -> None:
        self.screen.fill(self.background_color)
        for colony in world.colonies:
            for ant in colony.ants:
                image = pygame.transform.rotate(self._ant_image, ant.look_angle)
                self.camera.draw_image(image, (ant.position.x, ant.position.y), self.screen)
            if colony.nest is not None:
                self.camera.draw_image(
                    self._nest_image,
                    (colony.nest.position.x, colony.nest.position.y),
                    self.screen,
                )
        for food in world.food:
            self.camera.draw_image(
                self._food_image,
                (food.position.x, food.position.y),
                self.screen,
            )
            