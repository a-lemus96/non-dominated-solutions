# stdlib modules
import argparse

# thrid-party modules
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
points = ndsols.generate_set(50, 2, 9, 0.5)
# find non-dominated solutions using naive algorithm
non_dominated = ndsols.naive_algorithm(points)

# plot non-dominated solutions
plt.figure(figsize=(8,8))
plt.scatter(points[:, 0], points[:, 1])
plt.scatter(non_dominated[:, 0], non_dominated[:, 1])
plt.savefig("naive_2d.png")
#plt.close()

non_dominated = ndsols.dc_algorithm(points)

plt.figure(figsize=(8,8))
plt.scatter(points[:, 0], points[:, 1])
plt.scatter(non_dominated[:, 0], non_dominated[:, 1])
plt.savefig("dc_2d.png")
#plt.close()
plt.show()

"""points = ndsols.generate_set(500, 3, 9, 0.5)
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
points = ndsols.naive_ndset(points)
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
plt.show()
plt.savefig("3d.png")"""
