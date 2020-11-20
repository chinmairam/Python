import pandas as pd
csv_path="csv_file.csv"
df=pd.read_csv(csv_path)
df.head() #examine first 5 rows
print(df)
