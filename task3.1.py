list = [0,14,2,3,1,4,7,7,2,9,5]

def max(list):
    help_list = list
    for i in range(1,len(list)):
        if list[i]<list[i-1]:
            a= list[i]
            list[i]=list[i-1]
            list[i-1]=a
        else:
            continue
    return list[-1]


def sort(list):
    maxl = max(list)
    hlist= []
    sort_list=[]

    for i in range(0,maxl+1):
        hlist.append(0)

    for i in range(0,len(list)):

        hlist[list[i]]+=1

    for i in range(0,len(hlist)):

        if hlist[i]==0:
            continue

        for j in range(0,hlist[i]):

            sort_list.append(i)


    return sort_list

list1=sort(list)
print(list1)
# Сложность данного алгоритма сортировки = O(N)+O(N^2)