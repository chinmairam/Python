import csv      
with open('python.csv', mode='r') as csv_file1:    
    reader = csv.DictReader(csv_file1, fieldnames=['name','department','birtday_month'])    
    line_count = 0    
    for row in reader:    
        if line_count == 0:    
            print(f'The Column names are as follows {", ".join(row)}')    
            line_count += 1      
        print(f'\t{row["name"]} works in the {row["department"]}, department and was born in {row["birthday_month"]}.')    
        line_count += 1    
    print(f'Processed {line_count} lines.')    
