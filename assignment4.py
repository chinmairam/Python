import csv

with open('status.csv',mode='w',newline='') as csv_file:
    fieldnames = ['Name', 'Status', 'Income', 'FD_List','Asset_Value_Dict']
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name':'AAA','Status': 'Professional','Income': 800000,'FD_List': [12000, 45000,300000, 200000],'Asset_Value_Dict': {'House':4500000, 'Car':600000, 'Land':4000000, 'Jewels':1000000}})
    writer.writerow({'Name':'BBB','Status': 'Politician','Income': 10000000,'FD_List': [2000000, 1000000, 25000000],'Asset_Value_Dict': {'House':30000000, 'Car':2000000, 'Land':100000000, 'Jewels':25000000}})
    writer.writerow({'Name':'CCC','Status': 'Employee','Income': 700000,'FD_List': [500000, 200000, 150000],'Asset_Value_Dict': {'House':1000000, 'Jewels':250000}})


with open('status.csv',mode='r',newline='') as csv_file:
    employee_reader = csv.DictReader(csv_file)
    sum1 = 0
    sum2 = 0
    for row in employee_reader:
        if row['Status'] == 'Professional':
            try:
                for i in range(0,len(row['FD_List'])):
                    sum1 += int(row['FD_List'][i])
                for v in row['Asset_Value_Dict'].values():
                    sum2 += int(v)
                if sum1 > 10*int(row['income']) or sum2 > 25*int(row['Income']):
                    raise ValueError
            except ValueError:
                print('Name:',row['Name'])
                print("IT Raid Alert")
            else:
                print("Good")
                print('Name:',row['Name'],'\nStatus',row['Status'],'\nIncome',row['Income'],'\nFD_List',row['FD_List'],'\nAsset_Value_Dict',row['Asset_Value_Dict'])
        elif row['Status'] == 'Politician':
            try:
                for i in range(0,len(row['FD_List'])):
                    sum1 += int(row['FD_List'][i])
                for v in row['Asset_Value_Dict'].values():
                    sum2 += int(v)
                if sum1 > 10*int(row['Income']) and sum2 > 25*int(row['Income']):
                    raise ValueError
            except ValueError:
                print('Name:',row['Name'])
                print("Disproportionate Assets Alert")
            else:
                print("Good")
                print('Name:',row['Name'],'\nStatus',row['Status'],'\nIncome',row['Income'],'\nFD_List',row['FD_List'],'\nAsset_Value_Dict',row['Asset_Value_Dict'])
        elif row['Status'] == 'Employee':
            try:
                for i in range(0,len(row['FD_List'])):
                    sum1 += int(row['FD_List'][i])
                for v in row['Asset_Value_Dict'].values():
                    sum2 += int(v)
                if sum1 > 20*int(row['Income']) or sum2 > 25*int(row['Income']):
                    raise ValueError
            except ValueError:
                print('Name:',row['Name'])
                print("Scam Alert")
            else:
                print("Good")
                print('Name:',row['Name'],'\nStatus',row['Status'],'\nIncome',row['Income'],'\nFD_List',row['FD_List'],'\nAsset_Value_Dict',row['Asset_Value_Dict'])

                    
    
