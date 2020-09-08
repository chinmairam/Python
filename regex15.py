import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: \
       ERROR Performing upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
#print(re.search(regex, "99 elephants in a [cage]"))

# Extracting PID using regexes
def extract_pid(log_line):
    #regex = r"\[(\d+)\]"
    regex = r"\[(\d+)\]\: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    #return result[1]
    return "{} ({})".format(result[1],result[2])

print(extract_pid(log))
#print(extract_pid("99 elephants in a [cage]"))
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
