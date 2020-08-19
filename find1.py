dad = 'dadaddadaadada'

count, place =0,0
#find returns -1 on failure,index returns ValueError on failure
while dad.find('dad', place) >= 0:
    place = dad.find('dad',place) + 1
    count += 1
print(count)
