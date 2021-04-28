# 150. Decorators

from time import time


def hello():
    print('hello')


greet = hello
del hello

greet()

# hello()


def hello_again(func):  # Higher Ordr Function HOC
    func()


def greet_again():
    print('still here')


hello_again(greet_again)
print(hello_again(greet_again))

# 151. Higher Order Functions


def greet2():
    def func():
        return 5
    return func

# 152 Decorators 2

# def hello_a_third_freaking_time():
#     print('hello')


def my_decorator(func):
    def wrap_func():
        print('******')
        func()
        print('******')
    return wrap_func


@my_decorator
def hello_a_third_freaking_time():
    print('hello')


@my_decorator
def bye():
    print('see ya later')


hello_a_third_freaking_time()
bye()

print('2-----2')

hello_number_four = my_decorator(hello_a_third_freaking_time)
hello_number_four()

# 153. Decorators 3

print('3-----3')


def my_decorator_two(func):
    def wrap_func(*args, **kwargs):
        print('******')
        func(*args, **kwargs)
        print('******')
    return wrap_func


@my_decorator_two
def hello_with_greeting(greeting):
    print(greeting)


@my_decorator_two
def hello_with_greeting_emoji(greeting, emoji):
    print(greeting, emoji)


print('4-----4')

hello_with_greeting('hiii')
hello_with_greeting_emoji('hiii', ':)')

# 154. Why Do We Need Decorators


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
    for i in range(100000000):
        i*5


long_time()
