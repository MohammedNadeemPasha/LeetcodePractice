# Given an integer array nums, find the shortest continuous subarray which, if sorted in non-decreasing order,
# makes the whole array sorted. Return the length of this subarray.
# ex:- nums = [2,6,4,8,10,9,15]; O/P -> 5

def shortestSubarray(nums):
    if len(nums) <= 1:
        return 0

    n = len(nums)
    max_so_far = nums[0]
    right = -1

    for i in range(1, n):
        max_so_far = max(max_so_far, nums[i])
        if nums[i] < max_so_far:
            right = i

    if right == -1: 
        return 0

    min_so_far = nums[n - 1]
    left = 0

    for i in range(n - 2, -1, -1):
        min_so_far = min(min_so_far, nums[i])
        if nums[i] > min_so_far:
            left = i

    return right - left + 1

print(shortestSubarray([3, 2]))  # Output: 2
print(shortestSubarray([2,6,4,8,10,9,15]))  # Output: 5