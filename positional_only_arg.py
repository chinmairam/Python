# To specify positional-only arguments,you include a forward slash in your
#   function's arguments.
def number_length(x, /):
    return len(str(x))

print(number_length(2112))
#print(number_length(x=31557600)) #TypeError

