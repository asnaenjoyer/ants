import pygame
import pygame.math



class Food(pygame.sprite.Sprite):
    COLOR = (200, 45, 35)

    def __init__(self, x, y, amount) -> None:
        super().__init__()

        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, self.COLOR, (0, 0, 16, 16))

        self.rect = self.image.get_rect(
            center=(x, y)
        )

        self.position: pygame.Vector2 = pygame.Vector2(self.rect.centerx, self.rect.centery)

        self.amount : int = amount
        
        
    def take(self, amount):
        taken = min(amount, self.amount)
        self.amount -= taken
        if self.amount <= 0:
            self.kill()
        return taken