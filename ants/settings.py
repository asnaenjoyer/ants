from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    window_width: int = 800
    window_height: int = 600
    world_width: int = 1600
    world_height: int = 1200
    window_title: str = "Ants"
    fps: int = 60
    background_color: tuple[int, int, int] = (235, 235, 220)
