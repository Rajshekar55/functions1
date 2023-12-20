
# function call for multipe times

def raj() :
    print('Python')
    print('Welcome to Python')
    print('\n')

raj()
raj()
raj()



# different function names

def Python() :
    print('python is versatile language')


def pynat() :
    print('scripting language')

def pandas() :
    print('It is a type of excel data form')
    print()


Python()
pynat()
pandas()

# function can be called for another

def pandas() :
    print('Pnadas')
    numpy()

def numpy() :
    print('Numpy')
    print()


pandas()


''' cannot call the functions before it is defined

show1()
show2()

def show1() :
    print('helooo python')

def show2() :
    print('hellooo pynat')

'''

# function in another function

def state() :
    print('hello  TS')
    def city() :
        print('hlooo KMR')
        print()
    city()
state()




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


def add(a, b) :
    sum = a + b
    return sum
a = 25
b = 25
res = add(a,b)
print('Result =', res)
    
    









































