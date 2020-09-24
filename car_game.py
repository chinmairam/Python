from random import shuffle,choice

def game(x,change=False):
    doors = ['goat','goat','car']
    shuffle(doors)
    print(doors)

game(4)
