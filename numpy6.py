import numpy as np

np_city = np.array([[1.64, 71.78],
                    [1.37, 63.65],
                    [1.6, 55.09],
                    [2.04, 74.85],
                    [2.04, 68.72],
                    [2.01, 73.57]])

print(np_city)
print(np.mean(np_city[:,0]))
print(np.median(np_city[:,0]))
print(np.corrcoef(np_city[:,0], np_city[:,1]))
print(np.std(np_city[:,0]))

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city1 = np.column_stack((height, weight))

print(height)
print(weight)
print(np_city1)
