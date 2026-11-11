import pygame

from ants.entities.nest import Nest


class Ant(pygame.sprite.Sprite):
    COLOR = (75, 45, 35)

    def __init__(self, food_group: pygame.sprite.Group, nest: Nest, pos: pygame.Vector2, unit_size: int) -> None:
        super().__init__()
        self.image = pygame.Surface((unit_size * 3, unit_size), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.COLOR, (0, 0, unit_size, unit_size))
        pygame.draw.ellipse(self.image, self.COLOR, (unit_size, 0, unit_size, unit_size))
        pygame.draw.ellipse(self.image, self.COLOR, (unit_size * 2, 0, unit_size, unit_size))

        self.rect = self.image.get_rect(center=(pos.x, pos.y))
        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)
