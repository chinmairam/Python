def myfriendsfunction(name, age, profession):
   print("Name: ", name)
   print("Age: ", age)
   print("Profession: ", profession)
friendanne = {"name": "Anne", "age": 26, "profession": "Senior Developer"}
x = myfriendsfunction(**friendanne)
print(x)