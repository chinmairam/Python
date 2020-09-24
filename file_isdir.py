import os
dir = "website"
for name in os.listdir(dir):
    full_name = os.path.join(dir, name)
    print(full_name)
    if os.path.isdir(full_name):
        print(f"{full_name} is a directory")
    else:
        print(f"{full_name} is a file")
