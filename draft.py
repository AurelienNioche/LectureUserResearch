import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

np.random.seed(124)
k1, t1 = 1, 10
k2, t2 = 1.3, 14
x1 = np.random.gamma(k1, scale=t1, size=25)
x2 = np.random.gamma(k2, scale=t2, size=25)
print("x1", x1)
print("x2", x2)

n1 = len(x1)
n2 = len(x2)
ranked = stats.rankdata(np.concatenate((x1, x2)))
print("ranked value", ranked)

rank_x = ranked[0:n1]  # get the x-ranks
u1 = n1 * n2 + (n1 * (n1 + 1)) / 2.0 - np.sum(rank_x, axis=0)  # calc U for x1
u2 = n1 * n2 - u1  # remainder is U for x2

mean_rank = n1*n2/2.0
print("mean_rank", mean_rank)

sd = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0) # We assume that there is not tie here
print("sd", sd)

u = max(u1, u2)

x_min, x_max = mean_rank-300, mean_rank+300
mu, sigma = mean_rank, sd
x = np.linspace(x_min, x_max, 1000)
y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )

x_f = np.linspace(u, x_max)
y_f = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x_f - mu)**2 / (2 * sigma**2) )

y2 = (1 - stats.norm.cdf(x, loc=mu, scale=sigma))

fig, axes = plt.subplots(ncols=2, figsize=(16, 9))

ax1, ax2 = axes

ax1.plot(x, y)
ax1.fill_between(x_f, 0, y_f, color="red")
ax1.axvline(u, ls='--', color="red")
ax1.set_xlabel("u")
ax1.set_ylabel("PDF")

ax2.plot(x, y2, color="red")
ax2.axvline(u, ls='--', color="red")
ax2.set_xlabel("u")
ax2.set_ylabel("1 - CDF")

plt.show()