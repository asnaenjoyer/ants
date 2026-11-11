from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    window_title: str = "Ants"
    window_width: int = 800
    window_height: int = 600
    fps: int = 60
    background_color: tuple[int, int, int] = (235, 235, 220)

    world_width: int = 1600
    world_height: int = 1200
    unit_size: int = 16

    pheromone_cell_size: int = 25
    max_pheromone_concentration: float = 100.0
    pheromone_evaporation_rate: float = 0.5
    pheromone_deposit_amount: float = 25.0
