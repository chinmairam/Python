Lines = ["This is line A\n","This is line B\n","This is line C"]
with open("Example1.txt","r+") as File1:
    file_stuff = File1.read()
    print(file_stuff)
    for line in Lines:
        File1.write(line)

#print(File1.closed)
#print(file_stuff)
