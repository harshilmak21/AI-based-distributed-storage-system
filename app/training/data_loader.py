from pathlib import Path

import pandas as pd

from config import DATASET_PATH

def load_dataset(path : Path = DATASET_PATH) -> pd.DataFrame:

    if not path.exists():
        raise FileExistsError(f"Dataset not ffound : {path}")

    return pd.read_csv(path)