d = {'foo': 1, 'bar': 2, 'baz': 3}
while d:
    print(d.popitem())
# The .popitem() method removes one key-value pair from d and returns it as a tuple.
# So the body of this while loop displays the contents of d as tuples.
print('Done.')
