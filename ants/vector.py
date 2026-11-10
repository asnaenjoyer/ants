from dataclasses import dataclass
from math import hypot


@dataclass
class Vector2:
    x: float = 0
    y: float = 0

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector2":
        return self * scalar

    def __iadd__(self, other: "Vector2") -> "Vector2":
        self.x += other.x
        self.y += other.y
        return self

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y

    def length(self) -> float:
        return hypot(self.x, self.y)

    def normalize_ip(self) -> None:
        magnitude = self.length()
        if magnitude:
            self.x /= magnitude
            self.y /= magnitude

    def distance_to(self, other: "Vector2") -> float:
        return (self - other).length()
