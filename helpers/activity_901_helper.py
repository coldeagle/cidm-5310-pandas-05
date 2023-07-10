import pandas as pd
import numpy as np


def create_rand_series(index: list, raw_data: pd.DataFrame, fraction: float, seed: int):
    if seed is None:
        seed = len(raw_data)
    np.random.seed(seed)
    return pd.Series(np.random.choice(index, int(fraction * raw_data.shape[0]), replace=False))


def print_shape(label: str, val: str):
    print(f'{label}: {val}')