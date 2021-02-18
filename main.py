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

# Formatted Strings

name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' years old')
print(f'hi {name} You are {age} years old')
print('hi {}. You are {} years old'.format('Johnny', 55))
print('hi {}. You are {} years old'.format(name, age))
print('hi {1}. You are {0} years old'.format(name, age))
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))

selfish = 'me me me'
nums = '01234567'

# [start:stop:stepover]

print(selfish[0:2])
print(nums[0:8:2])
print(nums[1:])
print(nums[:5])
print(nums[::1])
print(nums[-1])
print(nums[::-1])
print(nums[::-2])

# Strings are immutable

# Built-In Functions

greet = 'hellloooo'

print(len(greet))
print(greet[0:len(greet)])

quote = 'to be or not to be'

print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))

# Booleans

print(bool(1))
print(bool(0))
print(bool('false'))

# Lists

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2.5, 'a', True]
amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])
# print(amazon_cart[2])

# List Slicing

amazon_cart2 = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart2[0::2])
print(amazon_cart2[0:2:1])

amazon_cart2[0] = 'laptop'
new_cart = amazon_cart2[:]
new_cart[0] = 'gum'
# print(amazon_cart2[0:3])
print(new_cart)
print(amazon_cart2)

# Matrix

matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9],
]
# matrix[0][1] = 2

basket = [1,2,3,4,5]

# adding
# new_list = basket.append(100)
basket.append(100)
basket.insert(3,100)
basket.extend([200, 300])
# print(new_list)
print(basket)

# removing
basket.pop()
print(basket)
basket.pop(0)
print(basket)
basket.remove(200)
print(basket)

basket2 = [1,2,3,4,5]
new_basket2 = basket2.pop(1)
print(new_basket2)

new_basket3 = basket2.clear()
print(new_basket3)
print(basket2)

# find (index)

print(basket.index(100))
print(basket.index(100, 0, 3))
# print(basket.index(100, 3, 5))

print(100 in basket)
print(basket.count(100))
# basket.sort()
print(sorted(basket))
print(basket)

basket.reverse()
print(basket)

basket.sort()
basket.reverse()
print(basket[::-1])
print(basket)

# print(range(1,100))
# print(list(range(1,100)))

sentence = ' '
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Pete'])
print(sentence)
print(new_sentence)

# list unpacking

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(d)
print(other)
