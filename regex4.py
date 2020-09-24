import re

result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)  # span changes

result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

# IGNORECASE
print(re.search(r"p.ng", "Pangea", re.IGNORECASE))


def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
