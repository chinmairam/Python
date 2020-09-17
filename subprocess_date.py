import os

cmd = "date"
x = os.popen(cmd)
print('Current date is:', x)
