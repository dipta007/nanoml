from datasets import load_from_disk, load_dataset, DatasetDict
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


def split_hf_dataset(dataset, val_size=0.1, test_size=0.1):
    """Split a Hugging Face dataset into train, validation, and test sets.

    Args:
        dataset (datasets.Dataset): The dataset to split.
        val_size (float | int, optional): The size of the validation set. Defaults to 0.1.
        test_size (float | int, optional): The size of the test set. Defaults to 0.1.

    Returns:
        datasets.DatasetDict: A dictionary containing the train, validation, and test sets.
    """
    train_val = dataset.train_test_split(test_size=val_size)
    val = train_val["test"]

    train_test = train_val["train"].train_test_split(test_size=test_size)
    train = train_test["train"]
    test = train_test["test"]

    return DatasetDict({"train": train, "val": val, "test": test})
