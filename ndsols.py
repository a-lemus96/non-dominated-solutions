# stdlib modules
from typing import Tuple

# third-party modules
import numpy as np
from numpy import ndarray

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

def naive_algorithm(sols: ndarray) -> ndarray:
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

def dc_algorithm(sols: ndarray) -> ndarray:
    """Find the set of non-dominated solutions for sets of 2D and 3D points
    using a divide and conquer approach. The algorithmic complexity is O(nlogn).
    ----------------------------------------------------------------------------
    Args:
        sols: set of solutions represented as a set of 2D or 3D points
    Returns:
        ndsols: set of non-dominated solutions"""
    n, d = sols.shape # retrieve number of samples and dimension
    if d == 2:
        # sort by f1 and f2, in that order
        sols = sols[np.lexsort((sols[:, 1], sols[:, 0]))]
        # perform call to recursive function
        ndsols, _ = solve_2d(sols)
    if d == 3:
        # sort by f1, f2 and f3, in that order
        sols = sols[np.lexsort((sols[:, 2], sols[:, 1], sols[:, 0]))]
        # sort by f2 and f3, in that order
        #idxs = np.lexsort((sols[:, 2], sols[:, 1]))
        
        # perform call to recursive function
        ndsols, _ = solve_3d(sols)

    return ndsols

def solve_2d(sorted_sols: ndarray) -> Tuple[ndarray, int]:
    """Recursive function to compute the number of non-dominated solutions in a
    sorted array of solutions by f1, f2 in that order.
    ---------------------------------------------------------------------------- 
    Args:
        sorted_sols: set of solutions sorted by f1, f2
    Returns:
        ndsols: set of non-dominated solutions
        low: lower value of f2 among all non-dominated solutions"""
    n, _ = sorted_sols.shape # retrieve number of samples
    if n <= 1: # terminal case
        return sorted_sols, np.min(sorted_sols[:, 1])
    left, right = np.array_split(sorted_sols, 2) # split array into two parts
    left, low = solve_2d(left) # find nd-sols in the left
    right, _ = solve_2d(right) # find nd-sols in the right
    # combine solutions
    rsize, _ = right.shape
    select = np.ones(rsize, dtype=bool)
    for idx in range(rsize):
        if low <= right[idx, 1]:
            select[idx] = False # reject solution
    ndsols = np.concatenate((left, right[select]), axis=0)
    
    return ndsols, np.min(ndsols[:, 1])

def solve_3d(sorted_sols: ndarray) -> Tuple[ndarray, int]:
    """Recursive function to compute the number of non-dominated solutions in a
    sorted array of solutions by f1, f2, f3, in that order.
    ---------------------------------------------------------------------------- 
    Args:
        sorted_sols: set of solutions sorted by f1, f2, f3
    Returns:
        ndsols: set of non-dominated solutions
        low: lower value of f3 among all non-dominated solutions"""
    n, _ = sorted_sols.shape # retrieve number of samples
    if n<= 1: # terminal case
        print(sorted_sols)
        return sorted_sols, idxs, np.min(sorted_sols[:, 2])
    left, right = np.array_split(sorted_sols, 2) # split array in halves
    lsize, _ = left.shape
    # solve left sub-problem
    left, low = solve_3d(left)
    # solve right sub-problem
    right, _ = solve_3d(right) 
    # join left and right and sort by f2 and f3
    join = np.concat(left, right)
    idxs = np.lexsort((join[:, 2], join[:, 1]))
    # traverse array of sorted indices by f2 and f3
    for idx in idxs:
        if idx < k:
            # it is an element from the left 
        else:
            # it is an element from the right
