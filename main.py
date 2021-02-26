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