# Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


def find_duplicates(list1):
    my_dict = {}
    for i in range(len(list1)):
        if list1[i] not in my_dict:
            my_dict[list1[i]] = 1
        else:
            my_dict[list1[i]] +=1
    
    dup_list = []
    for key, value in my_dict.items():
        if value > 1:
            dup_list.append(key)
    return dup_list

print(find_duplicates([-1, 0, 1, 0, -1, -1, 2, 2]))