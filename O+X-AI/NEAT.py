class brain():
    def __init__(self, layers: list[int]) -> None:
        self.neurodes: list[list[float]] = [[]]
        for layer in layers:
            self.neurodes.append([0 * i for i in range(layer)])
