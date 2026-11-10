import pygame


class Camera:
    def __init__(self, viewport_size: tuple[int, int], world_size: tuple[int, int]) -> None:
        self.viewport_width, self.viewport_height = viewport_size
        self.world_width, self.world_height = world_size
        self.offset = pygame.Vector2(0, 0)
        self.zoom = 1.0
        self._dragging = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button in (2, 3):
            self._dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button in (2, 3):
            self._dragging = False
        elif event.type == pygame.MOUSEMOTION and self._dragging:
            self.offset -= pygame.Vector2(event.rel) / self.zoom
            self._clamp_offset()
        elif event.type == pygame.MOUSEWHEEL and event.y:
            mouse_x = getattr(event, "mouse_x", None)
            mouse_y = getattr(event, "mouse_y", None)
            if mouse_x is None or mouse_y is None:
                mouse_x, mouse_y = pygame.mouse.get_pos()

            wheel_y = -event.y if getattr(event, "flipped", False) else event.y
            mouse_position = pygame.Vector2(mouse_x, mouse_y)
            world_position = self.offset + mouse_position / self.zoom
            self.zoom = max(0.1, min(self.zoom * (1.1 ** wheel_y), 5.0))
            self.offset = world_position - mouse_position / self.zoom
            self._clamp_offset()

    def apply(self, rect: pygame.Rect) -> pygame.Rect:
        return pygame.Rect(
            round((rect.x - self.offset.x) * self.zoom),
            round((rect.y - self.offset.y) * self.zoom),
            max(1, round(rect.width * self.zoom)),
            max(1, round(rect.height * self.zoom)),
        )

    def draw_group(self, group: pygame.sprite.AbstractGroup, surface: pygame.Surface) -> None:
        for sprite in group.sprites():
            rect = self.apply(sprite.rect)
            image = sprite.image
            if rect.size != image.get_size():
                image = pygame.transform.scale(image, rect.size)
            surface.blit(image, rect)

    def _clamp_offset(self) -> None:
        visible_width = self.viewport_width / self.zoom
        visible_height = self.viewport_height / self.zoom
        self.offset.x = max(0, min(self.offset.x, self.world_width - visible_width))
        self.offset.y = max(0, min(self.offset.y, self.world_height - visible_height))
