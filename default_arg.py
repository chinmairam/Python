import time

print(time.ctime()) # To get time as a readable string

def show_default(arg=time.ctime()):
    print(arg)
# default argument statements are executed only once.So,Time won't progress

show_default()
