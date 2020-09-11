import pandas as pd

result = []
for chunk in pd.read_csv('data.csv', chunksize = 1):
    result.append(sum(chunk['x']))

total = sum(result)
print(total)
