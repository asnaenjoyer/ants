from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    window_title: str = "Ants"
    window_width: int = 800
    window_height: int = 600
    fps: int = 60
    background_color: tuple[int, int, int] = (235, 235, 220)

    world_width: int = 2000
    world_height: int = 2000
    unit_size: int = 16

    pheromone_cell_size: int = 10
    max_pheromone_concentration: float = 100.0
    pheromone_evaporation_rate: float = 4
    pheromone_deposit_amount: float = 25.0
    food_detection_radius = 40
