__all__ = ["World", "WorldRenderer", "Camera", "WorldGenerator"]


def __getattr__(name: str):
    if name == "World":
        from .world import World

        return World
    if name == "WorldRenderer":
        from .world_renderer import WorldRenderer

        return WorldRenderer
    if name == "Camera":
        from .camera import Camera

        return Camera
    if name == "WorldGenerator":
        from .world_generator import WorldGenerator

        return WorldGenerator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
