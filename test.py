# stdlib modules
import argparse

# thrid-party modules
import numpy as np
from matplotlib import pyplot as plt

# custom modules
import ndsols


points = []
with open('data.txt', 'r') as f:
    n = int(f.readline()) # number of data points
    for k in range(n):
        pair = f.readline()
        coords = pair.split(" ")
        coords = [float(coord) for coord in coords]
        points.append(tuple(coords))

points = set(points) # use set datastructure to remove duplicated solutions
points = np.array(tuple(points))
# find non-dominated solutions using naive algorithm
non_dominated = ndsols.naive_ndset(points)

# plot non-dominated solutions
plt.scatter(points[:, 0], points[:, 1])
plt.scatter(non_dominated[:, 0], non_dominated[:, 1])
plt.savefig("nd_naive.png")
