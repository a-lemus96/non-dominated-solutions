# stdlib modules
import argparse

# thrid-party modules
import numpy as np

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
print(non_dominated.shape)
