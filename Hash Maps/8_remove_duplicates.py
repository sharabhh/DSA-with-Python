# You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.
# You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.
# Your function should not modify the original list, instead, it should create a new list with unique values and return it.

def remove_duplicates(my_list):
    new_list = list(set(my_list))
    return new_list

print(remove_duplicates([1,2,3,5,2,1]))