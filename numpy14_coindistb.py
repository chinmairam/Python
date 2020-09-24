import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails = []

for x in range(10000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])

#print(final_tails) # No.of tails thrown in a game of 10 tosses.

# matplotlib (histogram)
plt.hist(final_tails, bins = 10)
plt.show()
