filename = 'data.txt'

try:
    with open(filename) as f:
        for line in f:
            items = line.split(',')
            total = 0
            try:
                for item in items:
                    num = int(item)
                    total += num
                print("Total = " + str(total))
            except:
                print("Error converting to integer.",items)
except:
    print("Error opening file. " + filename)
finally:
    print("This is finally block. Code will execute no matter what.")
