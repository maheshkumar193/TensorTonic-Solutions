from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))
    mode = 0
    max_freq = 0
    
    for item, count in Counter(x).items():
        if (count > max_freq):
            mode = item
        elif (count == max_freq):
            mode = min(mode, item)    
        max_freq = count
    
    return {
        "mean": mean,
        "median": median,
        "mode": float(mode)
    }