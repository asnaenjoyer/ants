import pygame


class Camera:
    def __init__(self, viewport_size: tuple[int, int], world_size: tuple[int, int]) -> None:
        self.viewport_width, self.viewport_height = viewport_size
        self.world_width, self.world_height = world_size
        self.offset = pygame.Vector2(0, 0)
        self._dragging = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button in (2, 3):
            self._dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button in (2, 3):
            self._dragging = False
        elif event.type == pygame.MOUSEMOTION and self._dragging:
            self.offset -= pygame.Vector2(event.rel)
            self._clamp_offset()

    def apply(self, rect: pygame.Rect) -> pygame.Rect:
        return rect.move(-round(self.offset.x), -round(self.offset.y))

    def draw_group(self, group: pygame.sprite.AbstractGroup, surface: pygame.Surface) -> None:
        for sprite in group.sprites():
            surface.blit(sprite.image, self.apply(sprite.rect))

    def _clamp_offset(self) -> None:
        self.offset.x = max(0, min(self.offset.x, self.world_width - self.viewport_width))
        self.offset.y = max(0, min(self.offset.y, self.world_height - self.viewport_height))
