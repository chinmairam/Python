# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}# x is merged with y and if same value of x updated
print(z)
# {'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
  # z = dict(x, **y)
  # print(z)
    # -{'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right
