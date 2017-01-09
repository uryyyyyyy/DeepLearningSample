from typing import Any, List
import numpy as np

# Main
if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6]]  # type: List[Any]
    a = np.array([[1, 2, 3], [4, 5, 6]])  # type: np.ndarray
    b = a.flatten()  # type: np.ndarray
    print(b)
