from decorator2 import do_twice

@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

say_whee()
greet("World")
hi_pspk = return_greeting("PSPK")
print(hi_pspk)
