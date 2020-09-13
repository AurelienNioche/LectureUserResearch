import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np



m1, m2 = 100, 100
sd1, sd2 = 10, 10
n = 20

seed = 0

while True:
    np.random.seed(seed)
    x1 = np.random.normal(m1, scale=sd1, size=n)
    x2 = np.random.normal(m2, scale=sd2, size=n)
    print("x1", x1)
    print("x2", x2)

    thr = 0.05
    t, p = stats.ttest_ind(x1, x2, equal_var=True)
    can_reject = p < thr
    print(f"t={t}, p={p}, can reject={can_reject}")

    if can_reject:
        print(seed)
        break
    else:
        seed += 1