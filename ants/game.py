import pygame

from .camera import Camera
from .entities.ant import Ant
from .entities.food import Food
from .entities.nest import Nest
from .settings import Settings


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        self.camera = Camera(
            (self.settings.window_width, self.settings.window_height),
            (self.settings.world_width, self.settings.world_height),
        )
        pygame.display.set_caption(self.settings.window_title)
        self.clock = pygame.time.Clock()

        self.food = pygame.sprite.Group()
        self.food.add(Food(200, 150, 100))

        self.nest = pygame.sprite.GroupSingle(Nest(600, 400))  # type: ignore[arg-type]

        self.ants = pygame.sprite.Group()
        for _ in range(2):
            self.ants.add(Ant(self.settings, self.food, self.nest))

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
        self.ants.update(delta_time)
        self.food.update()
        self.nest.update()

    def _draw(self) -> None:
        self.screen.fill(self.settings.background_color)
        self.camera.draw_group(self.ants, self.screen)
        self.camera.draw_group(self.food, self.screen)
        self.camera.draw_group(self.nest, self.screen)
        pygame.display.flip()
