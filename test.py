# stdlib modules
import argparse
import time

# thrid-party modules
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# custom modules
import ndsols

N = 20 # number of testcases
MAX = 250
MIN = 200
step = (MAX - MIN) // N
sizes = np.array(range(MIN, MAX + 1, step)) # input sizes

fig, axs = plt.subplots(2, 1, figsize=(15,10))
titles = [100, 50]
for i, ratio in enumerate([0., 0.5]):
    nds_naive = [] # for storing naive algorithm running times
    nds_dc = [] # for storing divide and conquer algorithm  running times
    for n in sizes: 
        print(n)
        points = ndsols.generate_set(n, 2, 9, ratio) # generate random 2D points
        # compute execution time for naive algorithm
        start = time.time()
        _ = ndsols.naive_algorithm(points)
        end = time.time()
        nds_naive.append(end - start) # append time value

        # compute execution time for dc algorithm
        start = time.time()
        _ = ndsols.naive_algorithm(points)
        end = time.time()
        nds_dc.append(end - start) # append time value

    # plot 2D results
    axs[i].plot(sizes, nds_naive, label='Naive', linewidth=3,
                marker='x', markerfacecolor='black', markeredgecolor='black')
    axs[i].plot(sizes, nds_dc, label='D&C', linewidth=3,
                marker='o', markerfacecolor='white', markeredgecolor='black')
    axs[i].set_title(f"{titles[i]}% non-dominated points")
    axs[i].legend()

plt.savefig("times_2d.png")
plt.show()
exit()


'''points = ndsols.generate_set(500, 3, 9, 0.5)
fig = plt.figure()
ax = fig.add_subplot(1,2,1, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
nds = ndsols.naive_algorithm(points)
nds = nds[np.lexsort((nds[:, 2], nds[:, 1], nds[:, 0]))]
ax.scatter(nds[:, 0], nds[:, 1], nds[:, 2])

ax2 = fig.add_subplot(1,2,2, projection='3d')
ax2.scatter(points[:, 0], points[:, 1], points[:, 2])
nds2 = ndsols.dc_algorithm(points)
ax2.scatter(nds2[:, 0], nds2[:, 1], nds2[:, 2])
plt.show()'''
