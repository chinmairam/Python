def temp_convert(var):
   try:
      return int(var)
   except ValueError as v:
      print("The argument does not contain numbers: ", v)

# Call above function here.
print(temp_convert("123"))
temp_convert("xyz")
