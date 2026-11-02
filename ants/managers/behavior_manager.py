from .behavior_factory import BehaviorFactory


class BehaviorManager:
    def __init__(self, ant):
        self.ant = ant
        self.factory = BehaviorFactory(ant)
        self.current = None

    def change(self, name, **kwargs):
        self.current = self.factory.create(name, **kwargs)
        self.current.on_start()

    def update(self, delta_time):
        if self.current is not None:
            self.current.update(delta_time)