import pandas as pd

data = {
    "country" : ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital" : ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area" : [8.516, 17.10, 3.286, 9.597, 1.221],
    "population" : [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(data)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
print()
print(brics["country"])
print(type(brics["country"]))
print()
print(brics[["country"]])
print(type(brics[["country"]]))
print()
print(brics[["country", "capital"]])
print()
print(brics[1:4])
print()
print(brics.loc["RU"]) # Gives Pandas Series using loc
print()
print(brics.loc[["RU"]]) # Gives DataFrame
print()
print(brics.loc[["RU", "IN", "CH"]])
print()
# Gives Intersection of rows and columns
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])
print()
print(cars.loc[:,"drives_right"]) # Series
print()
print(brics.loc[:, ["country", "capital"]]) # DataFrame
print()
print(brics.iloc[[1]]) # Gives Pandas Series using iloc
print()
print(brics.iloc[[1,2,3]])
print()
print(brics.iloc[[1,2,3], [0,1]])
print()
print(brics.iloc[:, [0,1]])
