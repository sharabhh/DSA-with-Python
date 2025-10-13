# You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
# Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.
# The tests for this exercise assume that arr1 is the list being converted to a set.

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