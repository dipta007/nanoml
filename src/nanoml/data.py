from datasets import load_from_disk, load_dataset
from datasets.config import DATASET_STATE_JSON_FILENAME
from pathlib import Path


def load_dataset_flexible(dataset_path, **kwargs):
    """Load a dataset from a local path or from the Hugging Face Hub.

    Args:
        dataset_path (str): The path to the dataset.
        kwargs (dict): Additional arguments to pass to the load_from_disk or load_dataset function.

    Raises:
        Exception: If the dataset is not found.

    Returns:
        datasets.Dataset: The dataset.
    """
    try:
        if Path(dataset_path, DATASET_STATE_JSON_FILENAME).exists():
            return load_from_disk(dataset_path, **kwargs)
        else:
            return load_dataset(dataset_path, **kwargs)
    except Exception as e:
        raise e
