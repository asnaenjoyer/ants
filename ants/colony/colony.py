from ants.entities.nest import Nest
from ants.entities.ant import Ant

class Colony:
    def __init__(self):
        self.ants: list[Ant] = []
        self.nest : Nest | None = None

    def add_ant(self, ant: Ant) -> None:
        self.ants.append(ant)

    def add_nest(self, nest: Nest) -> None:
        self.nest = nest

    def update(self, delta_time: float) -> None:
        for ant in self.ants:
            ant.update(delta_time)