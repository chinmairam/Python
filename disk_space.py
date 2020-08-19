mport shutil #for disk usage
import psutil #for CPU usage
du = shutil.disk_usage("/")
print(du)
print(du.free/du.total*100) #free disk space
for i in range(0,5):
    cp = psutil.cpu_percent(0.1) #in 0.1 seconds,It varies
    print(cp)
