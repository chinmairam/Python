# lottery powerball

# 69/5 * 68/4 * 67/3 * 66/2 * 65/1 * 26

#       (69)! / 5!*(69-5)!*26
def odds(balls,pick,power=False):
    """Enter a regular balls, number of balls
picked, and if they are using a powerball, you will be asked
for the number of powerballs"""
    from math import factorial as fact
    p_ball = 1
    if power:
        p_ball = int(input("Enter number of powerballs: "))
    return (fact(balls))/(fact(5)*fact(balls-pick))*p_ball

# print("{:,}".format(odds(69,6,True
print(f"{odds(69,6):,}")
