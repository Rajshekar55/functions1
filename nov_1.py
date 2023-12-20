# Decorators


print('Title : ')
def str_title(raj) :
    def name() :
        str1 = raj()
        return str1.title()
    return name

def print_str() :
    return 'hi im from india'
print(print_str())

k = str_title(print_str)
print(k())

print()

print('Swapcase :')

def str_swapcase(raj) :
    def name() :
        str1 = raj()
        return str1.swapcase()
    return name

def print_str() :
    return 'hi iM fRom inDia'
print(print_str())

k = str_swapcase(print_str)
print(k())
