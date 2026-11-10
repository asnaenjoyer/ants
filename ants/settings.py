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

    num_ants: int = 5
    num_food: int = 5
    food_amount: int = 500
    nest_max_amount: int = 1000