a = True
b = False
c = False

if not a or b:
    print ("CORRECT ANSWER")
elif not a or not b and c:
    print ("MAYBE CORRECT ANSWER")
elif not a or b or not b and a:
    print ("MAYBE WRONG ANSWER")
else:
    print ("WRONG ANSWER")
