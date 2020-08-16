import pytz, datetime

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
hour = int(input("Enter a hour: "))
minute = int(input("Enter a minute: "))

# Converting to a date

users_time = datetime.datetime(year,month,day,hour,minute)

#print(users_time.isoformat())

cairo_timezone = pytz.timezone('Africa/Cairo')
london_timezone = pytz.timezone('UTC')
delhi_timezone = pytz.timezone('Asia/Kolkata')
sydney_timezone = pytz.timezone('Australia/Sydney')

#Converts users_time into UTC time

cairo_time = pytz.utc.localize(users_time).astimezone(cairo_timezone) 
london_time = pytz.utc.localize(users_time).astimezone(london_timezone)
delhi_time = pytz.utc.localize(users_time).astimezone(delhi_timezone)
sydney_time = pytz.utc.localize(users_time).astimezone(sydney_timezone)

print("Cairo Time is ",cairo_time.isoformat())
print("London Time is ",london_time.isoformat())
print("New Delhi Time is ",delhi_time.isoformat())
print("Sydney Time is ",sydney_time.isoformat())

