# Problem:- Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum 
# of at least k. If there is no such subarray, return -1.
# ex:- nums = [1], k = 1 ; O/P -> 1

from collections import deque
def shortestSubarray(nums,target):
  p=[0]*(len(nums)+1)
  for i in range(len(nums)):
    p[i+1]=p[i]+nums[i]
  d=deque()
  ans=len(nums)+1
  for i in range(len(p)):
    while d and p[i]-p[d[0]]>=target:
      ans = min(ans,i-d[0])
      d.popleft()
    while d and p[i]<=p[d[-1]]:
      d.pop()
    d.append(i)
  return ans if ans<=target else -1

print(shortestSubarray([84,-37,32,40,95],167)) #O/P -> 3

