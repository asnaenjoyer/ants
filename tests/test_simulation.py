import unittest

from ants.colony.colony import Colony
from ants.engine.world import World
from ants.entities.ant import Ant
from ants.entities.food import Food
from ants.entities.nest import Nest
from ants.settings import Settings
from ants.vector import Vector2


class SimulationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.settings = Settings(world_width=200, world_height=200)

    def test_ant_moves_without_graphics_objects(self) -> None:
        ant = Ant(self.settings, [], Nest(100, 100), Vector2(100, 100))
        ant.set_direction(Vector2(1, 0))

        ant.move(0.5)

        self.assertAlmostEqual(ant.position.x, 150)
        self.assertAlmostEqual(ant.position.y, 100)

    def test_food_is_detected_by_distance(self) -> None:
        food = Food(120, 100, 10)
        ant = Ant(self.settings, [food], Nest(100, 100), Vector2(100, 100))

        self.assertIs(ant.check_food([food]), food)
        self.assertIsNone(ant.check_food([Food(300, 100, 10)]))

    def test_world_removes_depleted_food_and_keeps_shared_food_list(self) -> None:
        world = World(self.settings)
        colony = Colony()
        nest = Nest(100, 100)
        colony.add_nest(nest)
        ant = Ant(self.settings, world.food, nest, Vector2(100, 100))
        colony.add_ant(ant)
        world.colonies.append(colony)
        food = Food(120, 100, 1)
        world.food.append(food)

        food.take(1)
        world.update(0)

        self.assertEqual(world.food, [])
        self.assertIs(ant.food_group, world.food)

    def test_nest_deposit_respects_capacity(self) -> None:
        nest = Nest(0, 0, max_amount=3)

        self.assertEqual(nest.deposit(5), 3)
        self.assertEqual(nest.amount, 3)


if __name__ == "__main__":
    unittest.main()
