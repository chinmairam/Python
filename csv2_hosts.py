import csv
hosts = [["Machine Name", "IP Address"],["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w', newline='') as hosts_csv:
    writer = csv.writer(hosts_csv, quoting=csv.QUOTE_ALL,
                        delimiter=';', quotechar='*')
    writer.writerows(hosts)


# quoting = csv.QUOTE_NONNUMERIC,

