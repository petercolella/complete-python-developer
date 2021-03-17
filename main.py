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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter('Alita', 21)
player2 = PlayerCharacter('Tom', 44)

print(player1.name)
print(player1.age)
player1.run()
print(player1)
print(player2)

player2.attack = 50

print(player2.attack)