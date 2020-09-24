import random
#number = [random.randint(1,5) for i in range(1,26)]
#numbers = [i for i in range(1,26)]
#random.shuffle(numbers)

shuffled = [14, 16, 7, 12, 22,
            11, 15, 2, 6, 20,
            13, 23, 18, 3, 4,
            9, 10, 25, 5, 17,
            1, 19, 8, 21, 24]
horses = [[],
          [],
          [],
          [],
          []]
#for i in range(5):
#    for j in range(5):
#        horses[j].append(shuffled.pop())
horses = [[24, 17, 4, 20, 22],
          [21, 5, 3, 6, 12],
          [8, 25, 18, 2, 7],
          [19, 10, 23, 15, 16],
          [1, 9, 13, 11, 14]]
for race in horses:
    race.sort()
    #race.sort(reverse=True)
    
for race in horses:
    print(race)

def last(x):
    return x[-1]

new_horses = sorted(horses,key=last,reverse=True)

print()
for race in new_horses:
    print(race)
