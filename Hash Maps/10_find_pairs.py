def find_pairs(arr1, arr2, target):
    set1 = set(arr1) # this will avoid repeatation
    final_list = []
    for num in set1:
        remaining = target - num
        if remaining in arr2:
            final_list.append((remaining, num)) 
    return final_list
        

a1 = [1,2,3]
a2 = [4,5,6]
t = 7
print(find_pairs(a1, a2, t))