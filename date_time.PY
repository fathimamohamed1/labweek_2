from datetime import datetime, date, time
from turtle import right 

today =date.today()
print (today)

tommorow= date(2020,8,19)
print (tommorow)

next_week=date.fromisoformat('2020-08-24')
print (next_week)

right_now =datetime.now()
print(right_now)
