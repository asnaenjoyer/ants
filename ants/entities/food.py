import pygame


class Food(pygame.sprite.Sprite):
    COLOR = (200, 45, 35)

    def __init__(self, x, y, unit_size) -> None:
        super().__init__()

        self.image = pygame.Surface((unit_size, unit_size), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.COLOR, (0, 0, unit_size, unit_size))

        self.rect = self.image.get_rect(center=(x, y))
        self.hitbox = self.rect
        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)
        