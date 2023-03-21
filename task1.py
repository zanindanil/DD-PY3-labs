from random import randint
list = [randint(-10, 10) for i in range(20)]
def search_min(list):

    list.sort()

    return list[0]



print(search_min(list))