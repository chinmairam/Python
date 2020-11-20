#Hangman

import random
words = ["apples","anaconda","jasmine","dynamite","stationery"]
sel=words[random.randint(0,4)]
print("Let's play hangman!!!\nYou have 5 chances")
length = len(sel)
lst = []
for i in range(0,length):
    lst.append("_")
chances = 5
filled = 0
while chances > 0 and filled != length:
    flag = 0
    ch = input("\nMake a guess: ")
    for index,i in enumerate(sel):
        if i == ch:
            lst[index] = ch
            filled += 1
            flag = 1
    if flag == 0:
        chances -= 1
        print("You have %d chances remaining"%chances)
    for i in lst:
        print(i + " ", end="")
if filled==length:
    print("Congrats, you won!!!")
else:
    print("Better luck next time")
