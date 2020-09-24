import random

while True:
    number = random.randint(1,20)
    print(number)
    try:
        guess = int(input("Please enter a guess: "))
        while guess != number:
            if guess > number:
                print("Please guess a smaller number.")
                guess = int(input("Please enter a guess: "))
            else:
                print("Please guess a larger number.")
                guess = int(input("Please enter a guess: "))
        else:
            print("You guessed the correct number.")
    except ValueError:
        print("Oops please enter a number.")
    #    print("You guessed the correct number.")
    q = input("Do you want to play again? y/n ").lower()
    if q[0] == 'n':
        break
    
