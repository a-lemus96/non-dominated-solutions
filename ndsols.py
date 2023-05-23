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

def generate_set(n: int, d: int, r: float, ratio: float = 0.) -> ndarray:
    """Generates a set of either 2D or 3D points among which a number is consi-
    dered to be a non-dominated solution. Reference Pareto front is considered
    to be the surface of the hypersphere (x - r)^2 + (y - r)^2 + (z - r)^2 = r^2
    where x, y, z in [0, r].
    ----------------------------------------------------------------------------
    Args:
        n: number of desired points
        d: dimension of datapoints
        r: radius of hypersphere
        ratio: ratio of dominated solutions to the total number of solutions
    Returns:
        points: (n, d)-shape ndarray containing the desired number of non-domi-
                nated solutions"""
    points = np.random.normal(size=(n, d)) # sample gaussian
    # normalize each point
    points /= np.linalg.norm(points, axis=-1)[:, np.newaxis]
    # fold points such that all points have negative coordinates
    points[points > 0] *= -1
    # draw sample of points to convert into non-dominated
    k = int(n*ratio) # number of contaminated points
    idxs = np.random.choice(len(points), size=k, replace=False)
    factors = np.random.rand(k) # factors to shrink selected points
    points[idxs] *= factors[:, np.newaxis]
    # scale samples and translate them
    points *= r
    points += r
    
    return points
