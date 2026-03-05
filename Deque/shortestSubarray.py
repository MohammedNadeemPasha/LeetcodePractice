# Problem:- Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum 
# of at least k. If there is no such subarray, return -1.
# ex:- nums = [1], k = 1 ; O/P -> 1

from collections import deque
def shortestSubarray(nums,target):
  d=deque()
  prefix_sum=0
  result=float('inf')
  for i in range(len(nums)):
    prefix_sum+=nums[i]
    d.append(prefix_sum)
    if abs(prefix_sum) >= abs(target):
      while(abs(prefix_sum)-d[0]>abs(target)):
        d.popleft()
        print(prefix_sum)
      result=min(result,len(d))
  if result == float('inf'):
    return -1
  return result

shortestSubarray([5],4)