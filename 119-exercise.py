class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Felix', 2)
cat2 = Cat('Garfield', 6)
cat3 = Cat('Morris', 10)

# print(cat1, cat2, cat3)


# Create a function that finds the oldest cat
cats = [cat1, cat2, cat3]

# print(cats[1:])

def findOldestCat(catList):
    oldestCat = catList[0]
    for cat in catList[1:]:
        if (cat.age > oldestCat.age):
            oldestCat = cat
    return oldestCat


# Print our: "The oldest cat is x years old.". x will be the oldest cat's age by using the function in #2.
print(f'The oldest cat is {findOldestCat(cats).age} years old.')