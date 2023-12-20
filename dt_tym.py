from datetime import date 

my_dt = date(1997,2,10)
print(my_dt)


from datetime import time

my_tym = time(8,34,10)
print(my_tym)


from datetime import datetime

dt_tm = datetime(1997,2,10,8,36,10)

print(dt_tm)

print()


import calendar


year = 2023
month = 10

print(calendar.month(year,month))

print()


print('Calendar')

year = int(input('Enter Year = '))

print(calendar.calendar(year))



print()


print('Calendar 2024')

print(calendar.calendar(2024))




year = 2000

print('Leap Year : ', calendar.isleap(year))


















