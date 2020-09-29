class test:
 def __init__(self):
  print("Instace (object) is Created")

 def __del__(self):
  print ("Instace (object) is  destroyed")
 
t=test()
del t
