# You are given nums and an index k.
#
# A good subarray is a continuous subarray that must include index k.
# The score of a subarray is:
# minimum value in subarray * length of subarray.
#
# Return the maximum possible score.
#
# ex:
# nums = [1,4,3,7,4,5], - Choose subarray [3,7,4,5],  Minimum value = 3, Length = 4, Score = 3 * 4 = 15
# k = 3
# O/P -> 15
#
# Idea:
# - Use a monotonic increasing stack.
# - Each stack item stores:
#   - value, earliest index where this value can start as the minimum
# - When current num is smaller than stack top:
#   - Pop values from the stack.
#   - Each popped value is the minimum for a range ending before current index.
#   - If that range contains k, update the answer.
# - Push the current num with its earliest valid start index.
# - After the loop, pop remaining values.
#   - Their range ends at len(nums).
#   - If the range contains k, update the answer.
# - Return the maximum score.

def maximumScore(nums, k) :
    result=0
    def isValid(i,j,mid):
        if i<=mid and mid <j:
            return True
        else:
            False
    stack=[]
    for i,num in enumerate(nums):
        if not len(stack):
            stack.append((num,i))
            continue
        if num > stack[-1][0]:
            stack.append((num,i))
            if isValid(i,i,k):
                result=max(result,num)
        else:
            min_start=len(nums)
            while len(stack) and num <= stack[-1][0]:
                curr_num,j=stack.pop()
                min_start=min(min_start,j)
                if isValid(j,i,k):
                    result=max(result,curr_num*(i-j))
            stack.append((num,min_start))
    while len(stack):
        curr_num,i=stack.pop()
        if isValid(i,len(nums),k):
            result=max(result,curr_num*(len(nums)-i))
    return result