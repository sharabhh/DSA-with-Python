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