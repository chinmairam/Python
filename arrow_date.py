import arrow
date = arrow.get('2020-01-18','YYYY-MM-DD')
print(date)
x = date.shift(weeks=+6).format('MMM DD YYYY')
print(f"Date after 6 weeks is: {x}")
