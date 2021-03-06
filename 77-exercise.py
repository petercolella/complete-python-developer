some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# temp_list = []
# for element in some_list:
#     if some_list.count(element) > 1 and temp_list.count(element) == 0:
#         temp_list.append(element)
# print(temp_list)

# temp_list = some_list.copy()
# for el in set(some_list):
#     temp_list.remove(el)
# print(temp_list)

# print([el for el in set(some_list) if some_list.count(el) > 1])

print(list(filter(lambda el: some_list.count(el) > 1, set(some_list))))