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

print('a > A','a' > 'A')
print('B > b','B' > 'b')
print(1 < 2 < 3 < 4)
print(1 < 2 >3 < 4)

print(not(True))
print(not(1 != 1))

print('---66---')
print(True == 1) # False incorrect
print('' == 1) # False 
print([] == 1) # False
print(10 == 10.0) # False incorrect
print([] == []) # False incorrect
print('------')
print(True is 1) # False
print('' is 1) # False 
print([] is 1) # False
print(10 is 10) # True
print(10 is 10.0) # False
print([] is []) # False

for item in 'Zero to Mastery':
    print(item)
for item in [1,2,3,4,5]: # {1,2,3,4,5} and (1,2,3,4,5) same
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

my_list = [1,2,3,4,5,6,7,8,9,10]
print(sum(my_list))

counter = 0
for item in my_list:
    counter = counter + item
print(counter)

# range

print(range(100))

for _ in range(10):
    print(_)
for _ in range(0,10,2):
    print(_)
for _ in range(10,0,-2):
    print(_)
print(list(range(10)))

# enumerate

for i,char in enumerate('Helllooo'):
    print(i, char)

for i,char in enumerate(list(range(100))):
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

my_list = [1,2,3]
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
my_list = [1,2,3]
for item in my_list:
    pass # continue
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass # continue

for item in my_list:
    pass # continue
    # print(item)

# Functions

def say_hello():
    print('Hello!')

say_hello()

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
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

print(add_two(4,5))

total = add_two(6,7)
print(total)
print(add_two(10,add_two(8,9)))

def add_two_outer(num1, num2):
    def add_two_inner(a, b):
        return a + b
    return add_two_inner(num1, num2)

print(add_two_outer(10,11))

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

print(super_func(1,2,3,4,5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs

def super_func_rule(name, *args, i='Hey', **kwargs):
    # print(*args)
    # print(args)
    total = 0
    print(f'{i} {name}')
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func_rule('Joe', 1,2,3,4,5, num1=5, num2=10))

# Walrus Operator

a = 'hellooooo'

if (len(a) > 5):
    print(f'too long {len(a)} elements')

if ((n := len(a)) > 5):
    print(f'too long {n} elements')

while ((n := len(a)) > 1):
    print(a, n)
    a = a[:-1]