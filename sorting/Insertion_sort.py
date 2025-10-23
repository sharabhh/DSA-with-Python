def insertion_sort(myList):
    for i in range(1,len(myList)):
        temp = myList[i]
        j = i-1
        while temp < myList[j] and j > -1:
            myList[j+1] = myList[j]
            myList[j] = temp
            j -= 1
    return myList

list1 = [9,8,7,6,5,4,3,1,2]
print(insertion_sort(list1))