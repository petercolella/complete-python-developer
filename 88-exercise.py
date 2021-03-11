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
print(highest_even([]))

# Official solution which breaks with empty list or all odd numbers

def highest_even_official(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even_official([10,2,3,4,8,11]))
print(highest_even_official([-10,-2,-3,-4,-8,-11]))
print(highest_even_official([3,5,11]))
print(highest_even_official([3,5,11,2]))
print(highest_even([]))