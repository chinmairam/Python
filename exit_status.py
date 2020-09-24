import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")

else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

# python exit_status.py example #example is a filename
# python exit_status.py text
