import os
import datetime
size = os.path.getsize("first_draft.txt")
print(f"File Size is {size}.")
time = os.path.getmtime("first_draft.txt")
print(f"Last modified (Timestamp) is {time}") # UNIX used this format of time
timestamp = os.path.getmtime("first_draft.txt")
exact_time = datetime.datetime.fromtimestamp(timestamp)
print(f"Correct time is {exact_time}")
# 1st datetime is module, 2nd is datetime class
