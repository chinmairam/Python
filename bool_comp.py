x = 8
y = 9
z = not(not(x < 3) and not(y > 14 or y > 10))
print(z)

""" not has a higher priority than and and or,
  it is executed first"""
# x < 3 is False. y > 14 or y > 10 is False
