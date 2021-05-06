# 165. Exercise: Fibonacci Numbers

# def fib_gen(number):
#     current = 1
#     previous = 0
#     for i in range(number + 1):
#         if i == 0 or i == 1:
#             yield i
#         else:
#             yield current + previous
#             temp = current
#             current = current + previous
#             previous = temp


def fib_gen(number):
    first = 0
    second = 1
    for _ in range(number + 1):
        yield first
        temp = first
        first = first + second
        second = temp


def fib_func(number):
    for item in fib_gen(number):
        print(item)


fib_func(20)

print('--------------------')


def fib_func_list(number):
    result = []
    for item in fib_gen(number):
        result.append(item)
    print(result)


fib_func_list(20)
