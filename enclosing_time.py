import time

def make_timer():
    last_called = None # Never
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed

print("t")
t = make_timer()
print(t())
print(t())
print(t())
print("t1")
t1 = make_timer()
print(t1())
print(t1())
print("t2")
t2 = make_timer()
print(t2())
print(t2())
