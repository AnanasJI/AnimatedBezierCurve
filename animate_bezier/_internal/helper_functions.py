from typing import Dict
import numpy as np
import pandas as pd

from .bezier import bezier


def create_df_dict(p: np.ndarray, ts: np.ndarray) -> Dict[int, pd.DataFrame]:
    column_names = ["t", "x", "y"]
    df_dict = {}

    for t in ts:
        points = p
        while len(points) > 0:
            points_append = np.hstack(
                (np.repeat(t, len(points)).reshape((len(points), 1)), points)
            )
            k = len(points)
            if k in df_dict:
                df_dict[k] = df_dict[k].append(
                    pd.DataFrame(points_append, columns=column_names)
                )
            else:
                df_dict[k] = pd.DataFrame(points_append, columns=column_names)
            points = bezier(points, t)
    return df_dict


def num_decimals(a: float) -> int:
    s = str(a)
    if "." not in s:
        return 0
    return len(s) - s.index(".") - 1
