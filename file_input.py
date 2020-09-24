f = open('text.txt', 'a')
print("Enter text data into file 'end' to stop")
while True:
    st = input()
    if(st == 'end'):
        break
    f.write(st+'\n')

f.close()

f = open('text.txt', 'r')
lines = f.read()
print(lines)
f.close()
