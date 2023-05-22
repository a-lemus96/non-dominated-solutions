# third-party modules
import numpy as np
from numpy import ndarray

def naive_ndset(sols: ndarray):
    """Naive algorithm for finding the set of non-dominated solutions for sets
    of 2D and 3D points. Algorithm evaluates all possible coordinate pairings.
    ----------------------------------------------------------------------------
    Args:
        sols: set of solutions represented as a set of 2D or 3D points
    Returns:
        ndsols: set of non-dominated solutions"""
    n, d = sols.shape # retrieve number of sols and dimension
    print(n, d)
    ndsols = []
    for i in range(n):
        for j in range(n):
            comparison = sum([True if sols[j][k] < sols[i][k] else False
                              for k in range(d)])
            if comparison == d:
                break
        if comparison < d: # solution is non-dominated
            ndsols.append(sols[i])

    return np.array(ndsols)
