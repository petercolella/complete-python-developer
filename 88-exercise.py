def highest_even(li):
    result = None
    for value in li:
        if value % 2 == 0:
            if not result:
                result = value
                continue
            if value > result:
                result = value
    return result

print(highest_even([10,2,3,4,8,11]))
print(highest_even([-10,-2,-3,-4,-8,-11]))
print(highest_even([3,5,11]))
print(highest_even([3,5,11,2]))