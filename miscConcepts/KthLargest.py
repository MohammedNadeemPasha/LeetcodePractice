#  Problem:- Given an unsorted integer array nums and an integer k, return the kth largest element in the array.
#  ex:- nums = [3,2,1,5,6,4], k = 2 ; O/P -> 5
# // ex:- nums = [3,2,3,1,2,4,5,5,6], k = 4 ; O/P -> 4
import heapq

def KthLargest(nums,k):
  heap = heapq.heapify(nums);result=[];output=0
  for i in range(len(nums)):
    if(len(result)>=k and result[0]<nums[i] ):
      heapq.heappop(result)
      heapq.heappush(result,nums[i])
    elif len(result)<k:
      heapq.heappush(result, nums[i])
  return heapq.heappop(result)

print(KthLargest([3,2,1,5,6,4],2)) #O/P -> 5
print(KthLargest([3,2,3,1,2,4,5,5,6],4)) #O/P -> 4