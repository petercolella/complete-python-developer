# 161. Generators

from time import time
range(100)
list(range(100))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


my_list = make_list(100)
print(my_list)

# 162. Generators 2

# iterable
# __iter__
# iterate
# generators are iterable


def generator_function(num):
    for i in range(num):
        yield i*2


for item in generator_function(1000):
    print(item)

g = generator_function(100)

print(next(g))
print(next(g))
print(next(g))

print('-------')


def generator_function_2(num):
    for i in range(num):
        yield i


g2 = generator_function(1)

print(next(g2))
# print(next(g2)) This causes the following error:

# Traceback (most recent call last):
#   File "/Volumes/Samsung USB/udemy/complete-python/section-10/main.py", line 50, in <module>
#     print(next(g2))
# StopIteration

# 163. Generators Performance


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Duration of function: {t2 - t1} seconds')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(10000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5


long_time()
long_time2()


def gen_fun(num):
    for i in range(num):
        yield i


for item in gen_fun(10):
    print(item)

# 164. Under The Hood of Generators


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break


special_for([1, 2, 3])


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration()


gen = MyGen(0, 100)
for i in gen:
    print(i)
