import numpy as np
import timeit

rand_nums = np.random.rand(1000)

#%timeit rand_nums
# To calculate runtime use %timeit
# x = timeit.timeit(sum(range(1000000)))
# print(x)
import timeit
print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a+b'))
