import pygame


class Nest(pygame.sprite.Sprite):
    COLOR = (35, 35, 20)

    def __init__(self, x: int, y: int, unit_size: int) -> None:
        super().__init__()

        self.image = pygame.Surface((unit_size * 3, unit_size * 3), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.COLOR, (0, 0, unit_size * 3, unit_size * 3))

        self.rect = self.image.get_rect(center=(x, y))
        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)
