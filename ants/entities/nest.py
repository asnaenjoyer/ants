import pygame


class Nest(pygame.sprite.Sprite):
    COLOR = (35, 35, 20)

    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.COLOR, (0, 0, 16, 16))

        self.rect = self.image.get_rect(
            center=(x, y)
        )

        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)

        self.amount : int = 0
        self.max_amount = 100
        
        
    def deposit(self, amount):
        free_space = self.max_amount - self.amount
        accepted = min(amount, free_space)
        self.amount += accepted
        return accepted