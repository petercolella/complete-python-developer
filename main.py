name = input('What is your name?')

print('Hello, ' + name)
# Fundamental Data Types
int
float
bool
str
list
tuple
set
dict

# Classes -> custom types

# Specialized Data Types

None

print(2 + 4)
print(type(2 + 4))
print(type(2 / 4))
print(2 ** 4)
print(9 // 4)
print(9 % 4)

# math functions
print(round(3.9))
print(abs(-20))

# operator precedence
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
print('hi {new_name}. You are {age} years old'.format(
    new_name='sally', age=100))

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
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9],
]
# matrix[0][1] = 2

basket = [1, 2, 3, 4, 5]

# adding
# new_list = basket.append(100)
basket.append(100)
basket.insert(3, 100)
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

basket2 = [1, 2, 3, 4, 5]
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

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(d)
print(other)

# Dictionary

dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': True
    }
]

print(my_list[0]['a'][2])
print(dictionary['a'][1])

# Dictionary Keys

dictionary = {
    123: [1, 2, 3],
    True: 'hello',
    # [100]: True
}

print(dictionary[123])
print(dictionary[True])
# print(dictionary[[100]])

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 57
}

print(user.get('age'))
print(user.get('age', 55))

user2 = dict(name='Peter')
print(user2)

print('basket' in user.keys())
print('hello' in user.values())
print(user.items())
print('bas' in user.items())
print([1, 2, 3] in user.items())
print(57 in user.items())

user3 = user.copy()
user.clear()
print(user)
print(user3)
print(user3.pop('age'))
print(user3)
print(user3.popitem())
print(user3)
print(user3.update({'basket': [4, 5, 6]}))
print(user3)

# Tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])
print(5 in my_tuple)

new_tuple = my_tuple[1:2]
print(new_tuple)
new_tuple2 = my_tuple[1:4]
print(new_tuple2)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(z)
print(other)

print(my_tuple.count(3))
print(my_tuple.index(3))
print(len(my_tuple))

# Set

my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)

my_temp_list = [1, 2, 3, 4, 5, 5]

print(set(my_temp_list))

print(1 in my_set)
print(len(my_set))
print(list(my_set))

new_set = my_set.copy()
print(new_set)
my_set.clear()
print(my_set)

set_one = {1, 2, 3, 4, 5}
set_two = {4, 5, 6, 7, 8, 9, 10}
set_three = {6, 7}

print('set methods')
# print(set_one.difference(set_two))
# print(set_one.discard(5))
# print(set_one)
# print(set_one.difference_update(set_two))
# print(set_one)
print(set_one.intersection(set_two))
print(set_one & set_two)
print(set_one.isdisjoint(set_two))
print(set_three.issubset(set_two))
print(set_two.issuperset(set_three))
print(set_one.union(set_two))
print(set_one | set_two)
is_old = True
is_licensed = True

if is_old and is_licensed:
    print('You are old enough to drive, and you have a license!')
# elif is_licensed:
#     print('You can drive now!')
else:
    print('You are not of age.')

print('okok')

# Ternary Operator

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting

is_Friend = False
is_User = True

print(is_Friend and is_User)

if is_Friend or is_User:
    print('best friends forever')

print('a > A', 'a' > 'A')
print('B > b', 'B' > 'b')
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4)

print(not(True))
print(not(1 != 1))

print('---66---')
print(True == 1)  # False incorrect
print('' == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # False incorrect
print([] == [])  # False incorrect
print('------')
print(True is 1)  # False
print('' is 1)  # False
print([] is 1)  # False
print(10 is 10)  # True
print(10 is 10.0)  # False
print([] is [])  # False

for item in 'Zero to Mastery':
    print(item)
for item in [1, 2, 3, 4, 5]:  # {1,2,3,4,5} and (1,2,3,4,5) same
    print(item)

# iterable - list, dictionary, tuple, set, string

user = {
    'name': "Golelm",
    'age': 5006,
    'can_swim': False
}

for key in user:
    print(key)

for thing in user.items():
    print(thing)
for thing in user.values():
    print(thing)
for thing in user.keys():
    print(thing)
for thing in user.items():
    key, value = thing
    print(thing)
for key, value in user.items():
    print(key, value)

# counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(my_list))

counter = 0
for item in my_list:
    counter = counter + item
print(counter)

# range

print(range(100))

for _ in range(10):
    print(_)
for _ in range(0, 10, 2):
    print(_)
for _ in range(10, 0, -2):
    print(_)
print(list(range(10)))

# enumerate

for i, char in enumerate('Helllooo'):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i)

# While Loop

i = 0
while i < 10:
    i += 1
    print(i)
    # break
else:
    print('done with the work')

my_list = [1, 2, 3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# while True:
#     input('say something: ')
#     break

# while True:
#     response = input('say sonething: ')
#     if (response == 'bye'):
#         break

print('-------')
my_list = [1, 2, 3]
for item in my_list:
    pass  # continue
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass  # continue

for item in my_list:
    pass  # continue
    # print(item)

# Functions


def say_hello():
    print('Hello!')


say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


def show_tree():
    for row in picture:
        print(''.join(['*' if num else ' ' for num in row]))


show_tree()


def say_hello_args(name, emoji):
    print(f'Hello, {name} {emoji}!')


# positional arguments
say_hello_args('Peter', '😀')

# keyword arguments
say_hello_args(emoji='😀', name='Peter')

# default parameters


def say_hello_default(name='Joe', emoji='😡'):
    print(f'Hello, {name} {emoji}!')


say_hello_default()
say_hello_default('Mama')

# return


def add_two(num1, num2):
    return num1 + num2


print(add_two(4, 5))

total = add_two(6, 7)
print(total)
print(add_two(10, add_two(8, 9)))


def add_two_outer(num1, num2):
    def add_two_inner(a, b):
        return a + b
    return add_two_inner(num1, num2)


print(add_two_outer(10, 11))

# Docstrings


def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)


test('!!!')

# help(test)
print(test.__doc__)

# Clean Code

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 != 0:
#         return False

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False


def is_even(num):
    return num % 2 == 0


print(is_even(3))

# *args **kwargs


def super_func(*args, **kwargs):
    # print(*args)
    # print(args)
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs


def super_func_rule(name, *args, i='Hey', **kwargs):
    # print(*args)
    # print(args)
    total = 0
    print(f'{i} {name}')
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func_rule('Joe', 1, 2, 3, 4, 5, num1=5, num2=10))

# Walrus Operator

a = 'hellooooo'

if (len(a) > 5):
    print(f'too long {len(a)} elements')

if ((n := len(a)) > 5):
    print(f'too long {n} elements')

while ((n := len(a)) > 1):
    print(a, n)
    a = a[:-1]
# OOP 115. What is OOP? Part 2


class BigObject:
    # code
    pass


print(type(BigObject))

obj1 = BigObject()  # instanciate
obj2 = BigObject()
obj3 = BigObject()

print(type(obj1))

# 116. Creating Our Own Objects


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        # if (age > 18):
        #     self.name = name # attributes
        #     self.age = age
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'My name is {self.name}')
        # print(f'My name is {PlayerCharacter.name}') Doesn't work

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Bobbie', num1 + num2)
        # return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Alita', 21)
player2 = PlayerCharacter('Tom', 44)

print(player1.name)
print(player1.age)
player1.run()
print(player1)
print(player2)

player2.attack = 50

print(player2.attack)

# 117. Attributes and Methods

# help(player1)

print(player1.membership)
player1.shout()

# 118. __init__

player3 = PlayerCharacter()
print(player3)
# print(player3.age) Throws error
# print(player3.name) Throws error

# 120. @classmethod and @staticmethod

# print(player1.adding_things(1, 2))
# print(PlayerCharacter.adding_things(3, 4))

player4 = PlayerCharacter.adding_things(3, 4)
print(player4.age)
print(player4.name)
print(player4)
print(player4.adding_things2(5, 6))

# 122. Developer Fundamentals: V


class PlayerCharacterSelf:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        self.name = name  # attributes
        self.age = age

    def run(self):
        return self

    def speak(self):
        print(f'My name is {self.name}, and I am {self.age} years old.')


player5 = PlayerCharacterSelf('Test', 1)
print(player5.run())
print(player5.run().run())

# 123. Encapsulation

player5.speak()

player6 = {'name': 'Peter', 'age': 57}
print(player6['name'])
print(player6['age'])

# 124. Abstraction

player5.name = '!!!'
# player5.speak = 'BOOO'

# player5.speak()

# 125. Private vs Public Variables


class PlayerCharacterPrivate:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        self._name = name  # attributes
        self._age = age

    def run(self):
        return self

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old.')


player7 = PlayerCharacterPrivate('Peter', 100)
player7.speak()

player7.name = 'Joe'
print(player7.name)
player7.speak()

# player7.speak = '!!!'
# print(player7.speak)

# 126. Inheritance


class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

# 127. Inheritance 2

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

# 128. Polymorphism


def player_attack(character):
    character.attack()


player_attack(wizard1)

user1 = User()

print('------------')

for character in [wizard1, archer1, user1]:
    player_attack(character)
    character.attack()
