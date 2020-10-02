def move_disk(n, src, dest, tmp):
    if n == 0:
        return
    else:
        move_disk(n-1, src, tmp, dest)
        print("Move disk", n, "from", src, "to", dest)
        move_disk(n-1,tmp, dest, src)

def main():
    print("***** TOWERS OF HANOI *****")
    print()
    num_disks = int(input("Enter number of disks: "))
    print()

    move_disk(num_disks, "A", "C", "B")

if __name__ == '__main__':
    main()
