def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    
    while i < len(list1):
        combined.append(list1[i])
        i+=1

    while j < len(list2):
        combined.append(list2[j])
        j+=1
    
    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    middle_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:middle_index])
    right = merge_sort(my_list[middle_index:])
    return merge(left, right)

unsorted_list = [9,3,6,2,5,1,4]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)