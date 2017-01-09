from typing import cast, Any, no_type_check

import matplotlib.pyplot as plt
import numpy as np


class Activator:

    @staticmethod
    def step(x: np.ndarray) -> np.ndarray:
        _x = cast(int, x)
        tmp = _x > 0
        _tmp = cast(np.ndarray, tmp)  # type: np.ndarray
        return np.array(_tmp, dtype=np.int)

    @no_type_check  # 型チェックはオペレータまで良い感じにできないっぽい？
    @staticmethod
    def sigmoid(x: float) -> np.ndarray:
        return 1 / (1 + np.exp(-x))

# Main
if __name__ == '__main__':
    step = Activator()  # type: Activator
    x = np.arange(-5.0, 5.0, 0.1)
    # y = step.step(x)
    y = step.sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
