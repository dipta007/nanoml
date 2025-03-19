import torch


def get_device() -> torch.device:
    """Get the device for the current system.

    Returns:
        torch.device: The device (torch.device("cuda"), torch.device("mps"), torch.device("cpu"))
    """
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def get_device_string() -> str:
    """Get the device string for the current system.

    Returns:
        str: The device string (cuda, mps, cpu)
    """
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def get_device_name() -> str:
    """Get the device name for the current system.

    Returns:
        str: The device name (e.g. "GeForce RTX 3090" or "Apple M1 Pro")
    """
    if torch.cuda.is_available():
        return torch.cuda.get_device_name()
    if torch.backends.mps.is_available():
        return torch.backends.mps.get_device()
    return "cpu"
