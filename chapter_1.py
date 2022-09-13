# In this chapter, I will practice hello world, variable, data type, data input, operator
# Comment, String manipulation

print('Hello World!')       # printing hello world
print("I am gonna be a pythonista !")

print()
print()

# ---------------------------------------Variable------------------------------------------------------

# Variable is a kind of box, where you can hold data, you can retrieve data and so on

name = "Eusha"
age = 33

# here, name& age are variables.............

print('My name is: ', name)
print('My age is: ', age)

print()
print()

x = 5
y = 6
z = x * y

# here, x, y & z are variables.................

print('Sum of x & y is: ', z)

print()
print()


# --------------------------------------- Data Type -------------------------------------------------------

# there are number if data types, some are discussed below.....................

name = "Mus'ab"    # string type.........
age = 25           # integer type........
height = 5.7       # float type .........
male = True        # bool type ..........

print(type(name))
print(type(age))
print(type(height))
print(type(male))

print()
print()

# --------------------------------------- Data Input ------------------------------------------------------

name = input('My name is :')        # input name from the keyboard ............
age = int(input('My age is: '))     # input age from the keyboard .............

print()
print()

# --------------------------------------- Type casting ----------------------------------------------------
x1 = '6'
y = 5

z = int(x1) + y    # here we convert string to int..................

print('Sum of x1 & y is: ', str(z))       # convert int ot str .....

print()
print()

# --------------------------------------- Operator --------------------------------------------------------

# arithmetic operator .................

x = 20
y = 5

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
exponent = x ** y
floor_division = x // y

print('Sum: ', addition)
print('Sub: ', subtraction)
print('Multi:', multiplication)
print('Div: ', division)
print('Rim: ', modulus)
print('Expo: ', exponent)
print('Floor: ', floor_division)
print()
print()

# comparison operator.....................

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# assignment operator =,+=, -=, *=,/=.......
# logical operator and, or , not ..........
# membership operator in & not in.............
# identity operator is, is not ........

print()
print()

# ----------------------------------------- String manipulation ---------------------------------

a = 'Banladesh'
print(a)
print(type(a))

print('I love my country \'bangladesh\' ')
print('I love my country \nbangladesh ')

print(a[2])
print(a[-1])
print(a[2:5])
print(a[0::2])

x = 'the'
y = 'king'

print(x + y)

print(' '.join((x, y)))

print(x.upper())
print(x.lower())
print(x.capitalize())
print(len(y))



