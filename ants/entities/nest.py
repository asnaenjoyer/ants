from ants.vector import Vector2


class Nest:
    SIZE = 16
    def __init__(self, x: int, y: int, max_amount: int = 100) -> None:
        self.position = Vector2(x, y)
        self.amount: int = 0
        self.max_amount = max_amount

    def deposit(self, amount: int) -> int:
        free_space = self.max_amount - self.amount
        accepted = min(amount, free_space)
        self.amount += accepted
        return accepted