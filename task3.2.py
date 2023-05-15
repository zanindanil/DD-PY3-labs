list = [0,14,2,3,1,4,7,7,2,9,5]

def sort_list(list):
    hlist=list
    k=len(list)
    p=0
    while True:

        for i in range(1, k):
            if list[i] < list[i - 1]:
                a = list[i]
                list[i] = list[i - 1]
                list[i - 1] = a
            else:
                continue
        k-=1
        if k == 0:
            break


    return list

lis = sort_list(list)

print(lis)