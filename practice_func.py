def world() :
    print('Helloo world...')
    def ind() :
        print('welcome to india')
        def ts() :
            print('it is a TS')
            def kmr() :
                print('from kmr')
                def per() :
                    print('Im Raj')
                per()
            kmr()
        ts()
    ind()
world()

print('\n')

def world() :
    print('hloo python world...')
    country()
def country() :
    print('Im from bharat')
    state()
def state() :
    print('TS state')
    city()
def city() :
    print('Kamareddy')
    person()
def person() :
    print('im Rajashekar')

world()


def operations() :
    print('arithmatic operations')
    def multi() :
        a = 5
        b = 10
        print('multiplication : ',a*b)
    def power() :
        a = 5
        b = 2
        print('Power a of b is :', a**b)
    def add() :
        x = 500
        y = 101
        print("adding : ", x+y)
    add()
    multi()
    power()
operations()



print()



'''
from datetime import date

my_dt = date(1997, 2, 15)

print('DOB         :    ',my_dt)



from datetime import time

my_tym = time(23, 2, 15)

print('time        :    ',my_tym)


from datetime import datetime

my_dttyme = datetime(1997, 2, 15, 23,2,15)

print('Date & Time :    ',my_dttyme)


print()

import calendar

yy = 2023
mm = 9

print(calendar.month(yy, mm))

print('Calendar 2023')

print(calendar.calendar(2023))

print('Calendar 2024')

print(calendar.calendar(2024))




year = 2024

print('Leap year : ',calendar.isleap(year))
'''



def first_last_char(raj) :
    print('original chars : ', raj)



    res = raj[0]

    l = len(raj)

    mi = int(l/2)

    res = res + raj[mi]

    res = res + raj[l - 1]

    print(res)

first_last_char('james')





















    
