#OOP 115. What is OOP? Part 2

class BigObject:
    # code
    pass

print(type(BigObject))

obj1 = BigObject() # instanciate
obj2 = BigObject()
obj3 = BigObject()

print(type(obj1))

# 116. Creating Our Own Objects

class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name # attributes
            self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'My name is {self.name}')
        # print(f'My name is {PlayerCharacter.name}') Doesn't work

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