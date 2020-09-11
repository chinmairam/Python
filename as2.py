a = {"R","HTML","Python"}
b = {".Net","Python","DW"}
c = {"Java","Informatics","Python"}
#1
x = a|b|c
list_of_strings = [str(s) for s in x]
joined_string = ",".join(list_of_strings)
print(joined_string)
#2
y = a & b &c
a = [str(s) for s in y]
b = ",".join(a)
print(b)



