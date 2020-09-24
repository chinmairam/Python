import pandas as pd

brics = pd.read_csv("brics.csv", index_col = 0)

for val in brics:
    print(val)

print()

for lab, row in brics.iterrows():
    print(lab)
    print(row)

print()

for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])

print()

for lab, row in brics.iterrows():
    # - Creating Series on every iteration
    brics.loc[lab, "name_length"] = len(row["country"])

for lab, row in brics.iterrows() :
    brics.loc[lab, "COUNTRY"] = row["country"].upper()
    
print(brics)

# More Efficient is to use apply() function 
brics["name_length1"] = brics["country"].apply(len)
brics["upper_case"] = brics["country"].apply(str.upper)
print(brics)

