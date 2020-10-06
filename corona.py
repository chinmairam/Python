print("GO CORONA GO")

count = 0
stuff = list()

while count < 5:
    num = input("Enter number of cases:")
    count += 1
    stuff.append(float(num))

avg = sum(stuff) / len(stuff)
print("Average", avg)
