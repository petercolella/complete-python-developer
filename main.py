from functools import reduce

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
