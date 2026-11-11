import pygame

from .engine.world_renderer import WorldRenderer
from .engine.world_generator import WorldGenerator
from .engine.world import World
from .engine.camera import Camera

from .settings import Settings


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption(self.settings.window_title)

        self.camera = Camera((self.settings.window_width, self.settings.window_height), 
                             (self.settings.world_width, self.settings.world_height), )

        self.world = World(self.settings)
        
        self.world_generator = WorldGenerator(self.settings)
        self.world_generator.generate(self.world)

        self.world_renderer = WorldRenderer(self.screen, self.camera, self.settings.background_color)

        self.clock = pygame.time.Clock()
        self.fps_update_timer = 0.0
        
        self.is_running = True

    def run(self) -> None:
        try:
            while self.is_running:
                delta_time = self.clock.tick(self.settings.fps) / 1000
                self._handle_events()
                self._update(delta_time)
                self._draw()
        finally:
            pygame.quit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            self.camera.handle_event(event)

    def _update(self, delta_time: float) -> None:
        self.world.update(delta_time)

        self.fps_update_timer += delta_time
        if self.fps_update_timer >= 0.5:
            fps = self.clock.get_fps()
            pygame.display.set_caption(f"{self.settings.window_title} | FPS: {fps:.0f}")
            self.fps_update_timer = 0.0

    def _draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.world_renderer.draw(self.world)
        pygame.display.flip()
