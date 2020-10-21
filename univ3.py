import pandas as pd
df = pd.DataFrame({'A':[2,3,5], 'B': [4,6,10]})
print(df.set_index('A').columns)
