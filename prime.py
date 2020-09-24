def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def nth_prime(x):
    num = 3
    prime = 2
    if x == 1 :
        return 2
    while prime < x:
        num += 2
        if is_prime(num):
            prime += 1
    return num

print(nth_prime(10)) #10th Prime Number

primes = [i for i in range(2,101) if is_prime(i)]

print(primes)
