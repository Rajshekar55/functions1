from abc import ABC


print('Sides of a Polygon')
class Polygon(ABC) :
    def sides(self) :
        pass
        

class Triangle(Polygon) :
    def sides(self) :
        print('Triangle has 3 sides')

t = Triangle()
t.sides()

class Square(Polygon) :
    def sides(self) :
        print('Square   has 4 sides')

s = Square()
s.sides()

class Pentagon(Polygon) :
    def sides(self) :
        print('Pentagon has 5 sides')

p = Pentagon()
p.sides()

class Hexagon(Polygon) :
    def sides(self) :
        print('Hexagon  has 6 sides')

h = Hexagon()
h.sides()

print()



print('Cars Collections :')


class Cars(ABC) :
    def models(self) :
        pass

class Rolles(Cars) :
    def models(self) :
        print('Rolles Royes Royal Cars')
r = Rolles()
r.models()

class Benz(Cars) :
    def models(self) :
        print('Mercedes benz car')

b = Benz()
b.models()


class Tata(Cars) :
    def models(self) :
        print('Tata motors')

t = Tata()
t.models()


print()

class Mobiles(ABC) :
    def brands(self) :
        pass

class OnePlus(Mobiles) :
    def brands(self) :
        print('OnePlus with 12 GB Ram')

o = OnePlus()
o.brands()





























