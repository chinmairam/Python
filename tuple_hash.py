if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    x = tuple(integer_list)
    print(x)
    print(hash(x))
