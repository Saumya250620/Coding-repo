def bubble(list1):
    l = len(list1) - 1
    sorted  = False

    while not sorted:
        sorted = True
        for i in range(0,l):
            if list1[i] > list1[i+1]:
                sorted = False
                list1[i],list1[i+1]=list1[i+1],list1[i]

    return list1

print(bubble([4,6,1,3,2,5,7,8,9]))
