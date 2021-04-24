from functools import reduce

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
# 138. Pure Functions


def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by_2([1, 2, 3]))

# 139 map()


def multiply_by_2_map(item):
    return item*2


my_list = [1, 2, 3]
print(list(map(multiply_by_2_map, my_list)))
print(my_list)

# 140 filter()


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

# 141 zip()

your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))

their_list = (5, 4, 3, 100)
print(list(zip(my_list, your_list, their_list)))

# 142 reduce()


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))

# 144. Lambda Expressions

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

# 146. List Comprehensions
# list, set, dictionary

my_list_comp = [char for char in 'hello']
my_list_comp2 = [num for num in range(0, 100)]
my_list_comp3 = [num*2 for num in range(0, 100)]
my_list_comp4 = [num**2 for num in range(0, 100) if num % 2 == 0]

# for char in 'hello':
#     my_list_comp.append(char)

print(my_list_comp)
print(my_list_comp2)
print(my_list_comp3)
print(my_list_comp4)

# 147. Set and Dictionary Comprehension

my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 100)}

print(my_set)
print(my_set2)

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
my_dict2 = {num: num*2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)
