#Computer Guessing Game - Bi-sectional Search(based on Mid Value)
ans = False

high = 100
low = 0

input('Think of a number between 1 and 100.Plase press enter to continue')

while not ans:
    guess = (high-low)//2 + low  #Ex:(100-50)//2 + 50 = 75
    print(f'Is your number {guess}')
    response = input("""Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate the guess is correct.
Enter Answer: """).lower()
    if response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    elif response == 'c':
        print('Thanks for playing with me!')
        ans = True
    
    
