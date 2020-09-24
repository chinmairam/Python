import random
def PasswordGenerator():
    lower_chars = ['a','b','c','d','e']
    upper_chars = ['A','B','C','D','E']
    special_chars = ['&','!','*']
    numeric_chars = ['1','2','3','4','5']
    
    password = random.choice(lower_chars) + random.choice(upper_chars) +random.choice(special_chars) + random.choice(numeric_chars)

    password = password + password

    return password

print(PasswordGenerator())
