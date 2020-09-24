from random import shuffle,choice

def game(x,change=False):
    doors = ['goat','goat','car']
    shuffle(doors)
    # print(doors)
    wins, losses = 0, 0

    def no_switch():
        nonlocal wins,losses
        if 'car' == choice(doors):
            wins += 1
        else:
            losses += 1

    def switch():
        door = ['goat','goat','car']
        nonlocal wins, losses
        door.pop(choice(range(3)))
        door.remove('goat')
        second_choice = door[0]
        if second_choice == 'car':
            wins += 1
        else:
            losses += 1

    for i in range(x):
        if change:
            switch()
        else:
            no_switch()
    print(f'wins: {wins} percent_wins: {(wins/x)}')
    print(f'losses: {losses} percent_losses: {(losses/x)}')

game(10000)
print()
game(10000,True)

            

