import torch


def is_bf16_supported() -> bool:
    """Check if bfloat16 is supported on the current device.

    Returns:
        bool: True if bfloat16 is supported, False otherwise.
    """
    major_version, _ = torch.cuda.get_device_capability()
    return major_version >= 8


def get_half_dtype() -> torch.dtype:
    """Get the half dtype for the current device.

    Returns:
        torch.dtype: The half dtype (torch.float16 or torch.bfloat16)
    """
    if is_bf16_supported():
        return torch.bfloat16
    return torch.float16


def get_half_dtype_string() -> str:
    """Get the half dtype string for the current device.

    Returns:
        str: The half dtype as a string (bfloat16 or float16)
    """
    if is_bf16_supported():
        return "bfloat16"
    return "float16"
