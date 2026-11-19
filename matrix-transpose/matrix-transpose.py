import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    rows = len(A)
    cols = len(A[0])
    A_transpose = np.zeros((cols, rows))

    for row in range(rows):
        for col in range(cols):
            A_transpose[col, row] = A[row][col]

    return A_transpose
