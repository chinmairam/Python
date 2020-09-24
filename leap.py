# leap year

def leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

years = [1992,1600,1900,2002,2020]

for year in years:
    print(year,leap_year(year))
