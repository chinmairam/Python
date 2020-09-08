import numpy as np

print(np.random.rand())  # Pseudo-rndom numbers

np.random.seed(123)
print(np.random.rand())
print(np.random.rand())

np.random.seed(123)
print(np.random.rand())
print(np.random.rand())  # Ensures "reproducibility"
