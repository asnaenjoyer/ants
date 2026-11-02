from ..behaviors.food_find import FoodFind
from ..behaviors.random_walk import RandomWalk
from ..behaviors.save_food import SaveFood
from ..behaviors.take_food import TakeFood
from ..behaviors.take_home import TakeHome


class BehaviorFactory:
    def __init__(self, ant):
        self.ant = ant

    def create(self, name, **kwargs):
        behaviors = {
            "random_walk": lambda: RandomWalk(self.ant, **kwargs),
            "food_find": lambda: FoodFind(self.ant, **kwargs),
            "take_food": lambda: TakeFood(self.ant, **kwargs),
            "take_home": lambda: TakeHome(self.ant, **kwargs),
            "save_food": lambda: SaveFood(self.ant, **kwargs)
        }

        if name not in behaviors:
            raise ValueError(f"Unknown behavior: {name}")

        return behaviors[name]()