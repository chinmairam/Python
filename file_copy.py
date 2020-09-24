def copyfile(oldfile, newfile):
    f1 = open(oldfile, "r")
    f2 = open(newfile, "w")
    while True:
        text = f1.read(50)
        if text == "":
            break
        f2.write(text)
    f1.close()
    f2.close()

copyfile('copy.txt','copy1.txt')
