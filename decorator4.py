def upper(func):
    def wrapper():
        return func().upper()
    return wrapper

@upper
def hi():
    return "Hi how are you?"

print(hi())
