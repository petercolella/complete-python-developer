# 138. Pure Functions

from functools import reduce


def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by_2([1, 2, 3]))

# 139 map()


def multiply_by_2_map(item):
    return item*2


my_list = [1, 2, 3]
print(list(map(multiply_by_2_map, my_list)))
print(my_list)

# 140 filter()


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

# 141 zip()

your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))

their_list = (5, 4, 3, 100)
print(list(zip(my_list, your_list, their_list)))

# 142 reduce()


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))

# 144. Lambda Expressions

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))
