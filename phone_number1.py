def phone_number():
    x = input("Enter your phone number: ")
    print(f'({x[:3]}){x[3:6]}-{x[6:]}')

def ssn():
    x = input("Enter your ssn: ")
    print(f'{x[:3]}-{x[3:5]}-{x[5:]}')

phone_number()
ssn()

