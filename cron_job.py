# Works on UNIX
from crontab import CronTab

my_cron = CronTab(username='your username')

for job in my_cron:
    print(job)

