import re

print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# Matching except alphabets
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# Alternative matches(one or more)
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like both dogs and cats."))

# To find all matches use findall function
print(re.findall(r"cat|dog", "I like both dogs and cats."))

import re
def check_punctuation (text):
  result = re.search(r"[,'.:?!;]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
