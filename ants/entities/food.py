from ants.vector import Vector2


class Food:
    SIZE = 16

    def __init__(self, x: float, y: float, amount: int) -> None:
        self.position = Vector2(x, y)
        self.amount: int = amount

    def take(self, amount: int) -> int:
        taken = min(amount, self.amount)
        self.amount -= taken
        return taken