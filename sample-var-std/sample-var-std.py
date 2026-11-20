import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x_mean = np.mean(x, dtype=np.float64)
    n = len(x)

    variance = sum((x_i - x_mean) ** 2 for x_i in x) / (n - 1)

    standard_deviation = np.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }