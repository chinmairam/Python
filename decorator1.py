def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say = my_decorator(say_whee)
#Simplest way is using @my_decorator instead of say = my_decorator(say_whee).It is called "Decorator"(“pie” syntax.). 
say()