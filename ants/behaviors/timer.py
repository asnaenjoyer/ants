class Timer:
    def __init__(self, interval : int) -> None:
        self._interval = interval
        self._time = 0

    def tick(self, delta_time : float) -> bool:
        self._time += delta_time

        if self._time >= self._interval:
            self._time -= self._interval
            return True

        return False

    def set_interval(self, interval):
        self._interval = interval
        self._time = 0