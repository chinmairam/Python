import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
random_walk = [0]

for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        #step = step - 1
        step = max(0,step - 1) # use max to make sure step can't go below 0
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

print(random_walk)

# matplotlib
plt.plot(random_walk)
plt.show()

# Use matplotlib in Jupyter Notebook for fast output
