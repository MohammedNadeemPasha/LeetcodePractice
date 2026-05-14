# You are given nums and threshold.
#
# Return the size of any subarray of length k where:
# every element > threshold / k
# Return -1 if no valid subarray exists.
#
# ex:
# nums = [1,3,4,3,1], Subarray [3,4,3] has length 3, Minimum value = 3, 3 * 3 > 6, so it is valid.
# threshold = 6
# O/P -> 3
#
# Idea:
# - Think of this like Largest Rectangle in Histogram.
# - For every number, try to use it as the smallest value of some subarray.
# - If nums[i] is the minimum of a subarray with length k,
#   then that subarray is valid when:
#       nums[i] * k > threshold
# - So we need to find the widest range where each number can remain the minimum.
# - Use a stack to keep numbers in increasing order.
# - When a smaller number appears, it means taller/larger values before it
#   cannot extend past this point.
# - For each removed value, calculate the length of the range where it was minimum.
# - If value * range_length > threshold, return that range length.
# - Add the current number back with the farthest left position it can cover.
# - At the end, check all remaining stack values using the array end as the boundary.
# - If none work, return -1.

def validSubarraySize(nums, threshold):
    def isValid(i,j,min_value):
        if min_value * (i - j)> threshold:
            return True
        return False
    q=[(nums[0],0)]
    for i in range(1,len(nums)):
        if nums[i]>=q[-1][0]:
            q.append((nums[i],i))
        else:
            last_pop=q[-1][1]
            while len(q) and nums[i]<q[-1][0]:
                curr_value,j=q.pop()
                last_pop=j
                if isValid(i,j,curr_value):
                    return i-j
            q.append((nums[i],last_pop))
    n = len(nums)
    while q:
        curr_value, j = q.pop()
        if curr_value * (n - j) > threshold:
            return n - j
    return -1