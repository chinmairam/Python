try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive integer")
except ValueError as ve:
    print(ve)
