from itertools import count, islice

def is_prime(x):
    if x > 1:
        for i in range(2,x):
            if x % i == 0:
                return  # Not a Prime
                break
        return x # Number is Prime

    else:
        return  # Number is < 1
    
thousand_primes = islice((x for x in count() if is_prime(x)),1000)
print(thousand_primes)
print(list(thousand_primes)[-10:])
print("Sum of first 1000 primes is: {}".format(sum(islice((x for x in count() if is_prime(x)),1000))))
print(any(is_prime(x) for x in range(1328, 1361)))
