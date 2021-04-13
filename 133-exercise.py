class SuperList(list):
    # def __init__(self, *args):
    #     list.__init__(self, *args)

    def __len__(self):
        return 1000


suprer_list1 = SuperList([1, 2, 3, 4])

print(len(suprer_list1))
suprer_list1.append(5)
print(suprer_list1)
print(len(suprer_list1))
