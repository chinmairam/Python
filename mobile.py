import re
s = "User's mobile number is 1234567890"
s_hide = re.sub('\d', '*', s)
print(s_hide)