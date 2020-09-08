import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups()) #('Lovelace', 'Ada')
print(result[0]) #Lovelace, Ada
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1]) #'Ada Lovelace'

def rearrange_name(name):
    #result = re.search(r"^(\w*), (\w*)$", name)
    #result = re.search(r"^([\w \.]*), ([\w \.]*)$",name)
    result = re.search(r"^([\w .-]*), ([\w .-]*)$",name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))
name=rearrange_name("Kennedy, John F.")
print(name)
