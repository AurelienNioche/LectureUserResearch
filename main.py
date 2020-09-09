import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

import seaborn as sns

# import statsmodels.formula.api as smf
#
df = pd.read_excel("data/RR.xlsx",
                   usecols=[0, 1, 2, 3],
                   names=['Country', 'Year', 'Debt', 'Growth'])

df.to_csv("data/rr.csv", index=False)
# df.head()
#
# df.plot.scatter(x="Debt", y="Growth", figsize=(16, 9))
# plt.show()
df = pd.read_csv(os.path.join("data", "rr.csv"))
#
df['DebtBin'] = pd.cut(df.Debt, bins=range(0, 250, 40), include_lowest=False)
y = df.groupby('DebtBin').Growth.mean()
print(type(list(y.index.values)[0]))
print()
print(list(y.values))
print(type(y))
x = [i.left + (i.right - i.left)/2 for i in y.index.values]
print(x)
ax = sns.barplot(x=x, y=y.values, palette="Blues_d")
ax.set_xlabel("Debt")
ax.set_ylabel("Growth")
plt.tight_layout()
plt.show()


df.plot.scatter(x="Debt", y="Growth", figsize=(16, 9))
# sns.displot(x="Debt", y="Growth", data=df, binwidth=3,)
# plt.show()


