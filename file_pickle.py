import pickle
with open("test.pck", "wb") as f:
    x = [1,2,3]
    pickle.dump(x,f)

with open("test.pck", "rb") as f:
    x = pickle.load(f)
    print(x)
