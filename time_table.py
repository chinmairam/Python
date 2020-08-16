def time_table():
    while True:
        try:
            x = int(input("Please enter a number: "))
            for row in range(x+1):
                for col in range(x+1):
                    print(f"{row*col:3}",end = " ")
                    #Space of 3 
                print()
        except ValueError:
            print("Oops! Please enter a number")
        q = input("Do you want another table? y/n" ).lower()
        if q[0] == 'n':
            break

time_table()
