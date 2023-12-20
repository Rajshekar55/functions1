# Encapsulation


class Mobiles :
    def __init__(self, brand, ram, price) :
        self.brand = brand
        self.ram = ram
        self.price = price
        
    def display(self) :
        print('Brand Name   : ', self.brand)
        print('Mobile Ram   : ', self.ram)
        print('Mobile Price : ', self.price)

mob = Mobiles('OnePlus', '12 GB', '28,000\n')
mob1 = Mobiles('Realme', '8 GB', '21,990\n')
mob2 = Mobiles('Nokia', '6 GB', '15,599\n')
mob3 = Mobiles('Lenovo', '6 GB', '18,999')


mob.display()
mob1.display()
mob2.display()
mob3.display()





