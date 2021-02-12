#Fundamental Data Types
int
float
bool
str
list
tuple
set
dict

#Classes -> custom types

#Specialized Data Types

None

print(2 + 4)
print(type(2 + 4))
print(type(2 / 4))
print(2 ** 4)
print(9 // 4)
print(9 % 4)

#math functions
print(round(3.9))
print(abs(-20))

#operator precedence
print(20 - 3 * 4)

# ()
# **
# * /
# + -

complex
print(bin(5))
print(int('0b101', 2))

# augmented assignment operator
some_value = 5
# some_value = some_value + 2
some_value += 2

print(some_value)

print(type('Hello world!'))
long_string = '''
WOW
0 0
---
'''

print(long_string)

first_name = 'Peter'
last_name = 'Colella'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation
print('hello' + ' Peter')
# print('hello' + 5)

# type conversion
print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)

# Escape Sequence
# weather = 'It\'s \'kind of\' sunny'
weather = '\t It\'s \'kind of\' sunny \n have a good day!'

print(weather)