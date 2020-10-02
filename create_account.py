"""1. open the create_account.py file that's in this folder:
2. Create and use a function to get a valid email address.
   To be valid, the address has to contain an @ sien and end with ".com".
3. Create and use a function to get a valid phone number.
   To do that, remove all spaces, dashes, parens, and periods from the number.
Then, check to make sure it the phone number consists of 10 characters that are digits.
4. When all of the entries are valid, display the message shown above,
   including the phone number format that uses dots to group the
   digits"""

def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    email = get_email()
    print()
    phno = get_phone_number()
    print()
    first_name = get_first_name(full_name)
    print("Hi " + first_name + ", thanks for creating an account.")
    print("We'll text your confirmation code to this number: ", phno)
    
def get_full_name():
    while True:
        name = input("Enter full name: ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_password():
    while True:
        password = input("Enter password: ")
        digit = False
        cap_letter = False
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password)<8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password

def get_first_name(full_name):
    index = full_name.find(" ")
    first_name = full_name[:index]
    return first_name

def get_email():
    while True:
        email = input("Enter Email Address: ")
        at_index = email.find("@")
        dotcomindex = email.find(".com", at_index)
        if at_index == -1 or dotcomindex == -1:
            print("Please enter a valid email address.")
        else:
            return email

def get_phone_number():
    while True:
        phno = input("Enter Phone Number: ")
        phno = phno.replace("-", " ")
        phno = phno.replace("(", "")
        phno = phno.replace(")", "")
        phno1 = phno
        phno = phno.replace(" ","")
        flag = 0
        try:
            if len(phno) < 10:
                raise ValueError
            phno = int(phno)
            flag = 1
        except ValueError:
            print("Enter 10 digit phone number")
        if flag:
            return phno1.replace(" ", ".")

if __name__ == '__main__':
    main()
