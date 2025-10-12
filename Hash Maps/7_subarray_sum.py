# Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).
# Your function should take two arguments:
# nums: a list of integers representing the input array
# target: an integer representing the target sum
# Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

def subarray_sum(nums, target):
    arr_map = { 0 : -1}
    sum = 0
    for i, num in enumerate(nums):
        sum += num
        if sum - target in arr_map:
            start = arr_map[sum-target] +1 
            end = i
            return [start, end]
        arr_map[sum] = i
    print(arr_map)
    return []

nums = [1, 2, 3, 4, 5]
target = 8
print(subarray_sum(nums, target))