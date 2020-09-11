with open('test.txt',"w") as f:
    f.write("lineone\nline two\nline three\n")

for f_obj in open('test.txt'):
    print(f_obj, end = '')
