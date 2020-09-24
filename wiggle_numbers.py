def wiggle_numbers(x):
    """Wiggle numbers:
    Given a list of number, return the list with all even numbers doubled,
    and all odd numbers turned negative."""
    wriggle = [i*2 if i % 2 == 0 else i*-1 for i in x]
    return wriggle

nums = wiggle_numbers([72, 26, 79, 70, 20, 68, 43, -71, 71, -2])
print(nums)
