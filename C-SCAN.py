def C_SCAN(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=200
	start=0
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	time+=abs(pos-end)
	pos=end
	#seek to hp from start
	for i in range(start,hp+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked")
			requests.remove(i)
	
	# calculate average seek time
	avg_seek_time = time/n
	return avg_seek_time

if __name__=='__main__':
	print("DISK SCHEDULING:")
	print("Provide number of I/O requests")
	#n is the number of I/O requests
	n = int(input())
	print("Provide initial position of disc arm (total cylinders=200)")
	hp = int(input())
	while hp>200:
		print("!!! INVALID !!! try again")
		hp = int(input())	
	print("Provide positions to visit : max is 200")
	requests = []
	for i in range(n):
		req = int(input())
		requests.append(req)

	print(requests)

	print("  **********     C-SCAN     *********")
	print("Avg seek time for  C-scan was ",
		C_SCAN(hp,requests))
