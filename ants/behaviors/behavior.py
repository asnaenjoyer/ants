class Behavior:
    def __init__(self, ant) -> None:
        self.ant = ant

    def on_start(self):
        pass

    def update(self, delta_time : float):
        raise NotImplementedError