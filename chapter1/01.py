from typing import Any, List
import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    __w1 = 0.5
    __w2 = 0.5
    __theta = 0.7

    def add(self, x1: int, x2: int) -> int:
        tmp = x1*self.__w1 + x2*self.__w2  # type: float
        if tmp <= self.__theta:
            return 0
        elif tmp <= self.__theta:
            return 1

# Main
if __name__ == '__main__':
    p = Perceptron()  # type: Perceptron
    r1 = p.add(0, 0)  # type: int
    print(r1)
