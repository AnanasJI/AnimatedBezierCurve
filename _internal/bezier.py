import numpy as np


def bezier(p: np.ndarray, t: float) -> np.ndarray:
    next_p = p[1:]
    p = p[:-1]
    return (1 - t) * p + t * next_p
