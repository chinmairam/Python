from pprint import pprint as pp
m = {'H': [1,2,3],
     'He': [3,4],
     'Li': [6,7]}
m['H']+=[4,5,6,7]
print(m)
m['Be'] = [7,9,10]
print("After inserting ",m)
print()
print("Better display using pprint ")
print(pp(m))
