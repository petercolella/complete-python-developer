# Error Handling
# 156. Errors in Python

# def hooohooo() # SyntaxError: invalid syntax


# pass


# def second():
#     1 + name  # NameError: name 'name' is not defined


# second()

# def third():
#     li = [1, 2, 3]
#     li[5]  # IndexError: list index out of range


# third()

# def fourth():
#     dict = {'a': 1}
#     dict['b']  # KeyError: 'b'


# fourth()

# def fifth():
#     5/0  # ZeroDivisionError: division by zero


# fifth()

# 157. Error Handling

while True:
    try:
        age = int(input('What is your age?'))
        10/age
        print(age)
    except ValueError:
        print('Please enter a number.')
    except ZeroDivisionError:
        print('Please enter age above zero.')
    else:
        print('Thank you!')
        break

# 158. Error Handling 2


def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print('Please enter numbers.', err)
        print(f'Please enter numbers. {err}')  # Both print the same thing.


print(sum(1, 2))


def divide(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print('Your error is:', err)
        print(f'Your error is: {err}')  # Both print the same thing.


print(divide(1, 0))
