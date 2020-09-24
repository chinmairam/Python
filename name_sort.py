def take_char(name):
    return name[3]

L = ['RAMA','LAKSHMANA','BHARATHA','CHATHTRUGUNA']
L.sort(key=take_char)
print(L)
