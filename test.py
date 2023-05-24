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

# configure parser
parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=20,
                    help='Number of testcases')
parser.add_argument('--d', type=int, default=2,
                    help='Number of testcases')
parser.add_argument('--max', type=int, default=50000,
                    help='Upper end of input size interval')
parser.add_argument('--min', type=int, default=200,
                    help='Lower end of input size interval')
# parse arguments
args = parser.parse_args()

step = (args.max - args.min) // args.n
sizes = np.array(range(args.min, args.max + 1, step)) # input sizes

fig, axs = plt.subplots(2, 1, figsize=(15,10))
titles = [100, 50]
for i, ratio in enumerate([0., 0.5]):
    nds_naive = [] # for storing naive algorithm running times
    nds_dc = [] # for storing divide and conquer algorithm  running times
    for n in sizes: 
        print(n)
        # generate random (2D or 3D) points
        points = ndsols.generate_set(n, args.d, 9, ratio) 
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

plt.savefig(f"times_{args.d}d.png")

# generate 3D points to visualize output
points = ndsols.generate_set(500, 3, 9, 0.)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
nds = ndsols.dc_algorithm(points)
ax.scatter(nds[:, 0], nds[:, 1], nds[:, 2], label='Non-dominated')
ax.set_title("500 non-dominated 3D points out of 500")
ax.legend()
plt.savefig("sample_3D.png")

# generate 2D points to visualize output
fig = plt.figure(figsize=(6,6))
points = ndsols.generate_set(50, 2, 9, 0.5)
ax2 = fig.add_subplot(1,1,1)
ax2.scatter(points[:, 0], points[:, 1])
nds2 = ndsols.dc_algorithm(points)
ax2.scatter(nds2[:, 0], nds2[:, 1], label='Non-dominated')
ax2.set_title("25 non-dominated 2D points out of 50")
ax2.legend()
plt.savefig("sample_2D.png")
