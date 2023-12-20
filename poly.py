# Ploymorphism


class Breeza() :
    def btype(self) :
        print('Car')
    def bcolor(self) :
        print('White')
    def bSpeed(self) :
        print('200kmph')
    def bFuel(self) :
        print('Petrol')


class Ducati(Breeza) :
    def type(self) :
        print('Bike')
    def color(self) :
        print('Green\n')
    def fuel(self) :
        print('Diesel')


d = Ducati()
d.type()
d.fuel()
d.color()
d.btype()
d.bcolor()
d.bSpeed()
d.bFuel()



class A:
    def m1(self) :
        print('welcome to python')

def monkey_function(self) :
    print('WELCOME to PYthon')



print()

print('Mobile Specifications :')

class Oneplus:
    def type(self):
        print('Branded phone')
    def color(self):
        print('gray and blue')
    def price(self) :
        print(29,995)
    def storage(self) :
        print('256 GB')


class realme(Oneplus) :
    def rtype(self):
        print('Android TV')
    def rprice(self) :
        print(21,599)


x = realme()

x.type()
x.rtype()































