import re

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"A.*a", "Australia"))

#Variable Pattern Validation
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable name"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

""" starts with an uppercase letter, followed by at least some
lowercase letters or a space,and ends with a period,
question mark, or exclamation point."""
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][ |a-z]*[.?\!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
