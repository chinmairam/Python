##with open('software.csv') as software:
##    reader = csv.DictReader(software)
##    for row in reader:
##        print(("{} has {} users").format(row["name"], row["users"]))
##

import csv

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT"},
          {"name": "Lio Nelson", "username": "lion", "department": "User Experience"},
          {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
