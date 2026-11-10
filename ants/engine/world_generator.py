from .world import World

class WorldGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate(self, world):
        ...