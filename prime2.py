def prime(num):
    d = []
    for i in range(2,num):
        if num % i == 0:
            d.append(i)

    if len(d) > 0:
        print("Not a Prime")
    else:
        print("Prime")

prime(3)
prime(10)
prime(11)
