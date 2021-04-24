a = 1

def confusion():
    a = 5
    return a

def parent():
    a = 10
    def child():
        return a
    return child()

print(confusion()) # 5
print(a) # 1
print(parent()) # 10

total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count())

total1 = 0

def count1(total):
    total += 1
    return total

print('dependency injection', count1(count1(count1(total1))))

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()

#1 - Start with local
#2 - Parent local
#3 - Global
#4 - Built in python functions