# Divide and Conquer for Finding Non-dominated Solutions

In multi-objective optimization, several objective functions must be optimized simultaneously. One of the steps in multi-objective optimization algorithms is to detect the set of non-dominated solutions among a discrete set of solutions. This repository contains a divide and conquer (D&C) implementaion for determining the set of non-dominated solutions for the cases of two and three objective funtions whose running times are $O(n\log_2 n)$ and $O(n(\log_2 n)^2)$, in that order. The performance of the algorithms are compared to their naive counterparts, which run in $O(n^2)$.

### Data Generation
One way to generate a set of 3D solutions in which we can control the rate of non-dominated solutions is to draw samples from the surface of the sphere defined by $(x - r)^2 + (y - r)^2 + (z - r)^2 = r^2$ for $x, y, z \in [0, r]$. Points generated in this way are guaranteed to be non-dominated (you can prove this by contradiction). The same idea is used for the 2D case, but using $(x - r)^2 + (y - r)^2= r^2$ for $x, y \in [0, r]$. Then, we can shrink the length of some points such that a specific portion is guaranteed to be non-dominated. Here is an example of a 2D set with 25 non-dominated solutions out of 50 using $r=9$:

![sample_2D](https://github.com/a-lemus96/non-dominated-solutions/assets/95151624/93dff999-55c5-416d-9639-082863afd7cb)

and here is an example of a 3D set with 500 non-dominated solutions out of 500 using $r=9$:

![sample_3D](https://github.com/a-lemus96/non-dominated-solutions/assets/95151624/b1471818-dbd3-496e-bf9b-2548fdcca5bf)

### Running Time Tests
For each dimension, two main cases were evaluated: 1) All the points are non-dominated and 2) half of the points are non-dominated. This leads to a total of 4 main tests. In each test, 20 evenly spaced input sizes were chosen from the interval $[200, 50\times 10^3]$, a set of random points with the specified proportion of non-dominated solutions was generated and both algorithms where applied (naive and D&C). Execution times for each algorithm on each input size were taken. Here are the plot for the results from the 2D case:



And, these are the results from the 3D case:

