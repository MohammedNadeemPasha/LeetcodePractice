# Problem:- Given an array of integers nums, return true if there exists a 132 pattern 
# (nums[i] < nums[k] < nums[j] for i < j < k), otherwise return false.
# ex:- nums = [1,2,3,4] ; O/P -> false
# ex:- nums = [3,1,4,2] ; O/P -> true

from collections import deque

def find132pattern(nums):
    if len(nums)<3:
        return False
    dq=deque()
    second=float('-inf')
    for i in range(len(nums)-1,-1,-1):
        if nums[i]>=second:
            while len(dq) and dq[-1]<nums[i]:
                second = dq.pop()
            dq.append(nums[i])
        else:
            return True
    return False

print(find132pattern([1,2,3,4])) # O/P -> False
print(find132pattern([6,12,3,4,6,11,20])) # O/P -> True (6,12,11)