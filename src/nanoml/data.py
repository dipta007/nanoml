from datasets import load_from_disk, load_dataset
from datasets.config import DATASET_STATE_JSON_FILENAME
from pathlib import Path


def load_dataset_flexible(dataset_path: str, *args, **kwargs):
    """Get the appropriate dataset loader based on the dataset path.

    Args:
        dataset_path (str): The path to the dataset.

    Raises:
        Exception: If the dataset is not found.

    Returns:
        datasets.Dataset: The dataset.
    """
    try:
        if Path(dataset_path, DATASET_STATE_JSON_FILENAME).exists():
            return load_from_disk(dataset_path, *args, **kwargs)
        else:
            return load_dataset(dataset_path, *args, **kwargs)
    except Exception as e:
        raise e
