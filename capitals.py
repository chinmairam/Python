import csv

##with open('capitals.csv') as f:
##    r = csv.reader(f, delimiter=',')
##    for row in r:
##        if len(row) == 2:
##            print(row[0] + ', ' + row[1])

states = ['Tripura', 'West Bengal']
caps = ['Agartala', 'Kolkata']

##with open('capitals.csv', 'a', newline='') as f:
##    w = csv.writer(f, delimiter=',')
##    for i in range(len(states)):
##        w.writerow([states[i], caps[i]])

##with open('capitals.csv', 'a', newline='') as f:
##    w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
##    for i in range(len(states)):
##        w.writerow([states[i], caps[i]])

with open('capitals.csv', 'r') as f:
    print(' ')
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row['State'] + ", " + row['Capital'])
