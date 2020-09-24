import pandas as pd
import numpy as np

# brics = pd.read_csv("brics.csv")
brics = pd.read_csv("brics.csv", index_col = 0)
print(brics.loc[:,"area"])
is_huge = brics["area"] > 8
print(is_huge)
print(brics[is_huge])
# print(brics[brics["area"] > 8])
print(np.logical_and(brics["area"] > 8, brics["area"] < 10))
print(brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)])
