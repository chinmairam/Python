# python3
from random import randint

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    x = max(numbers)
    numbers.remove(x)
    y = max(numbers)
    return x * y

def max_pairwise_stress(n,m):
    while True:
        n = randint(2,n)
        arr = [None]*n
        for i in range(n):
            arr[i] = randint(0,m)
        print(arr)
        x1 = max_pairwise_product(arr)
        x2 = max_pairwise_product_fast(arr)
        if x1 == x2:
            print("Ok")
        else:
            print("Wrong Answer",x1,x2)
            return

if __name__ == '__main__':
    max_pairwise_stress(1000,900000)
    """input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))"""
