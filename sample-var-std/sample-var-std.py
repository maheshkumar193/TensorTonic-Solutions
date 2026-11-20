import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x, dtype=np.float64)
    x_mean = np.mean(x, dtype=np.float64)
    centered = x - x_mean
    
    variance = np.sum(centered ** 2) / (x.size - 1)

    standard_deviation = np.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }