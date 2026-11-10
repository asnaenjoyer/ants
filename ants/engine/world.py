from ants.entities.food import Food
from ants.settings import Settings
from ants.colony.colony import Colony


class World:
    def __init__(self, settings: Settings) -> None:
        self.food: list[Food] = []
        self.colonies: list[Colony] = []
        self.settings = settings

    def update(self, delta_time: float) -> None:
        for colony in self.colonies:
            colony.update(delta_time)
        self.food[:] = [food for food in self.food if food.amount > 0]
