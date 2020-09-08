import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

np.random.seed(4)

mean_1 = 150.0
mean_2 = 200.0

small_std = 10.0
large_std = 50.0

n = 100

val1_small_std = np.random.normal(mean_1, scale=large_std, size=n)
val2_small_std = np.random.normal(mean_2, scale=large_std, size=n)

val1_large_std = np.random.normal(mean_1, scale=small_std, size=n)
val2_large_std = np.random.normal(mean_2, scale=small_std, size=n)

fig, axes = plt.subplots(ncols=2, nrows=2)

i = 0
for val1, val2 in zip((val1_small_std, val1_large_std), (val2_small_std, val2_large_std)):
    print("i", i)

    ax = axes[i, 0]
    sns.distplot(val1, ax=ax, color="C0")
    sns.distplot(val2, ax=ax, color="C1")

    ax.axvline(np.mean(val1), label="mean", color='C0', lw=2, ls='--')
    ax.axvline(np.mean(val2), label="mean", color='C1', lw=2, ls='--')

    ax.set_ylabel("Proportion")
    ax.set_xlabel("value")

    ax = axes[i, 1]

    df = pd.DataFrame({
        "x": val1,
        "y": val2
    }).melt()

    sns.barplot(x="variable", y="value", ax=ax, data=df, ci="sd")

    ax.set_ylim(0, max(mean_1, mean_2) + large_std * 1.25)
    ax.axhline(mean_1, ls='--', color='black', alpha=0.1, lw=2)
    ax.axhline(mean_2, ls='--', color='black', alpha=0.1, lw=2)

    i += 1

plt.show()