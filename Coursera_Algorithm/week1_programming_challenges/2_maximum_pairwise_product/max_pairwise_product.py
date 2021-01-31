# python3

def max_pairwise_product_fast(numbers):
    x = max(numbers)
    numbers.remove(x)
    y = max(numbers)
    return x * y

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
