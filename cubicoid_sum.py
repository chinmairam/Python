if __name__ == '__main__':
    x = int(input("Enter value of x:"))
    y = int(input("Enter value of y:"))
    z = int(input("Enter value of z:"))
    n = int(input("Enter value of n:"))

    print([[i, j, k] for i in range(x+1) for j in range(y+1)
          for k in range(z+1) if i+j+k != n])

# Sum should not be equal to n value
