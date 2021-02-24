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