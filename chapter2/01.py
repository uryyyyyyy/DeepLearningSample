import numpy as np


class Perceptron:
    # def __init__(self):
    #     self.__name = name

    @staticmethod
    def add_old(x1: int, x2: int) -> int:
        w1: float = 0.5
        w2: float = 0.5
        theta: float = 0.7
        tmp: float = x1*w1 + x2*w2
        if tmp <= theta:
            return 0
        else:
            return 1

    @staticmethod
    def add(x1: int, x2: int) -> int:
        w1: float = 0.5
        w2: float = 0.5
        theta = -0.7
        x = np.array([x1, x2])
        w = np.array([w1, w2])
        tmp: float = np.sum(x*w) + theta
        if tmp <= 0:
            return 0
        else:
            return 1

    @staticmethod
    def nand(x1: int, x2: int) -> int:
        w1: float = -0.5
        w2: float = -0.5
        theta: float = 0.7
        x = np.array([x1, x2])
        w = np.array([w1, w2])
        tmp: float = np.sum(x * w) + theta
        if tmp <= 0:
            return 0
        else:
            return 1

# Main
if __name__ == '__main__':
    p: Perceptron = Perceptron()
    r1: int = p.add(0, 0)
    print(r1)
    r2: int = p.add(1, 1)
    print(r2)

    r3: int = p.nand(0, 0)
    print(r3)
    r4: int = p.nand(1, 1)
    print(r4)
