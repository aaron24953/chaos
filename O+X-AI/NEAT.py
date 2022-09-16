# need the structure of the gene string, hex code input ideal

class Brain:
    def __init__(self, layers: list[int], genome: str) -> None:
        n=3
        nodes: list[list[int]] = []
        for layer in layers:
            nodes.append([0 * i for i in range(layer)])
        neurons: list[Neuron] = [Neuron(gene) for gene in [genome[i:i+n] for i in range(0, len(genome), n)]])

    def output(self, inp: list[float]) -> list[float]:
        return [0]


class Neuron:
    def __init__(self, gene: str) -> None:
        self.start =
        self.end =
        self.layer =
        self.operation =
        self.weight =
