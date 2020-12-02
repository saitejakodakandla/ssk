from datetime import datetime

futuredate = datetime.strptime('Nov 1 2021  13:33', '%b %d %Y %H:%M')

nowdate = datetime.now()
countdown = int((futuredate-nowdate).total_seconds())

days = countdown//86400
hours = (countdown-days*86400)//3600
minutes = (countdown-days*86400-hours*3600)//60
seconds = countdown-days*86400-hours*3600-minutes*60
print("{} days {} hours {} minutes {} seconds left".format(days, hours, minutes, seconds))
