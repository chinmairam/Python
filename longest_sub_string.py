x = 'abcaafahbaabdfgz'

sub = x[0]

long, length = sub, 1

for letter in x[1:]:
    if ord(sub[-1]) <= ord(letter):
        sub += letter
        if len(sub) > length:
            length = len(sub)
            long = sub
            print(long)
    else:
        sub = letter
#        print(letter)
print(long)
