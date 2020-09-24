import numpy as np

np.random.seed(123)

step = 50
dice = np.random.randint(1,7)

if dice <= 2 :
    step = step - 1
elif dice <= 5:
    step += 1
else:
    # Throw dice again.
    step = step + np.random.randint(1,7)
    
print(dice)
print(step)
