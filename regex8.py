import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r".com", "mydomain.com"))
print(re.search(r"\w*","This is an example"))
print(re.search(r"\w*","And_this_is_another"))

'''code to check if the text passed has at least 2 groups of
alphanumeric characters (including letters, numbers,
andunderscores) separated by one or more whitespace characters.'''
import re
def check_character_groups(text):
  result = re.search(r"[0-9]\w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
