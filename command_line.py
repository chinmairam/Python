import sys

# print(sys.argv)

# if len(sys.argv) > 1:
#    print(f"Hello {sys.argv[1]}")
#    print(sys.argv)
#else:
#    print(f"Hello World!")

if len(sys.argv) == 2:
    print(f"Hello {sys.argv[1]}")
    print(sys.argv)
elif len(sys.argv) == 3:
    print(f"Hello {sys.argv[1]}, I hear you are {sys.argv[2]}")
    print(sys.argv)
else:
    print(f"Hello World!")
    print(sys.argv)
