def highest_even(li):
    result = 0
    for value in li:
        if value % 2 == 0:
            if value > result:
                result = value
    return result

print(highest_even([10,2,3,4,8,11]))