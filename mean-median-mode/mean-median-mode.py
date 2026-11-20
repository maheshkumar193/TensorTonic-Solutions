from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))
    counts = Counter(x)
    max_freq = max(counts.values())
    mode = min(key for key, val in counts.items() if val == max_freq)
    return {
        "mean": mean,
        "median": median,
        "mode": float(mode)
    }