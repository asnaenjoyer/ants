import pygame


class Nest(pygame.sprite.Sprite):
    COLOR = (35, 35, 20)

    def __init__(self, x: int, y: int, unit_size: int) -> None:
        super().__init__()

        self.image = pygame.Surface((unit_size, unit_size), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.COLOR, (0, 0, unit_size, unit_size))

        self.rect = self.image.get_rect(center=(x, y))
        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)
