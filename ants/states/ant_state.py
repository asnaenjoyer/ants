from abc import ABC, abstractmethod
from ants.pheromones.pheromone_type import PheromoneType


class AntState(ABC):
    def __init__(self, ant):
        self.ant = ant
        self.pheromone_type: PheromoneType
        self.target_pheromone_type: PheromoneType

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass