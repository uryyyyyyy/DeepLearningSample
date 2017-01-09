import numpy as np

class Perceptron:
    # def __init__(self):
    #     self.__name = name

    @staticmethod
    def add_old(x1: int, x2: int) -> int:
        w1 = 0.5  # type: float
        w2 = 0.5  # type: float
        theta = 0.7  # type: float
        tmp = x1*w1 + x2*w2  # type: float
        if tmp <= theta:
            return 0
        else:
            return 1

    @staticmethod
    def add(x1: int, x2: int) -> int:
        w1 = 0.5  # type: float
        w2 = 0.5  # type: float
        theta = -0.7  # type: float
        x = np.array([x1, x2])
        w = np.array([w1, w2])
        tmp = np.sum(x*w) + theta  # type: float
        if tmp <= 0:
            return 0
        else:
            return 1

    @staticmethod
    def nand(x1: int, x2: int) -> int:
        w1 = -0.5  # type: float
        w2 = -0.5  # type: float
        theta = 0.7  # type: float
        x = np.array([x1, x2])
        w = np.array([w1, w2])
        tmp = np.sum(x * w) + theta  # type: float
        if tmp <= 0:
            return 0
        else:
            return 1

# Main
if __name__ == '__main__':
    p = Perceptron()  # type: Perceptron
    r1 = p.add(0, 0)  # type: int
    print(r1)
    r2 = p.add(1, 1)  # type: int
    print(r2)

    r3 = p.nand(0, 0)  # type: int
    print(r3)
    r4 = p.nand(1, 1)  # type: int
    print(r4)
