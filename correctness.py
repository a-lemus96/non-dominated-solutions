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

# configure parser
parser = argparse.ArgumentParser()
parser.add_argument('--datapath', type=str,
                    help='Datapath for input file')
parser.add_argument('--method', type=int, default=1,
                    help='1 for naive and 2 for DaC')
# parse arguments
args = parser.parse_args()

points = []
with open(args.datapath, 'r') as f:
    n = int(f.readline()) # number of data points
    for k in range(n):
        pair = f.readline()
        coords = pair.split(" ")
        coords = [float(coord) for coord in coords]
        points.append(tuple(coords))

points = set(points) # use set datastructure to remove duplicated solutions
points = np.array(tuple(points))
if args.method == 1:
    # find non-dominated solutions using naive algorithm
    non_dominated = ndsols.naive_algorithm(points)
elif args.method == 2:
    # find non-dominated solutions using DaC algorithm
    non_dominated = ndsols.dc_algorithm(points)

with open('results.txt', 'w') as f:
    f.write(str(len(non_dominated))+'\n')
    for i in range(len(non_dominated)):
        lst = [str(x) for x in non_dominated[i]]
        f.write(f"{' '.join(lst)}\n")
