from typing import Any, List
import numpy as np

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
