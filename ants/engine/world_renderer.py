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
        for colony in world.colonies:
            self.camera.draw_group(colony.ants, self.screen)
            if colony.nest is not None:
                self.camera.draw_sprite(colony.nest, self.screen)
        self.camera.draw_group(world.food, self.screen)
            