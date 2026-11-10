import pygame

from .camera import Camera
from .world import World


class WorldRenderer:
    def __init__(self, screen: pygame.Surface, camera: Camera, background_color) -> None:
        self.screen = screen
        self.camera = camera
        self.background_color = background_color

    def draw(self, world: World) -> None:
        background_rect = self.camera.apply(world.background.get_rect())
        self.screen.fill(self.background_color, background_rect)
        self.camera.draw_group(world.ants, self.screen)
        self.camera.draw_group(world.food, self.screen)
        self.camera.draw_group(world.nest, self.screen)