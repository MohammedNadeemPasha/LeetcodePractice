# You are given nums and k.
#
# Each number has a prime score: number of distinct prime factors.
#
# In one operation:
# - Pick a subarray.
# - Choose the element with the highest prime score.
# - If tied, choose the smallest index.
# - Multiply score by that element.
#
# Return the maximum score after at most k operations.
# ex:- Input: nums = [8,3,9,3,8], k = 2, Output: 81 -> [9],[9,3]
# Idea:
# - First calculate the prime score of every number.
# - For each index, find how many subarrays would choose nums[i].
# - Use a monotonic stack on prime scores to find the valid range for each index:
#   - Left side stops at a value with prime score >= current.
#   - Right side stops at a value with prime score > current.
#   - This handles the tie rule: smaller index wins.
# - The number of subarrays where nums[i] is chosen is:
#       (i - left) * (right - i)
# - Then greedily use the largest nums[i] values first.
# - Use a max heap to process bigger numbers before smaller ones.
# - For each number, use it up to its available subarray count.
# - Multiply it into the answer as many times as possible until k becomes 0.
# - Use pow(num, count, MOD) for fast multiplication.
# - Return answer modulo 10^9 + 7.

import heapq
def maximumScore(nums, k):
    ranges=[]
    prime_scores=[]
    heap=[]
    result=1
    def findPrimeFactors(num):
        factors=set()
        i=2
        while i * i <= num:
            if num % i == 0:
                factors.add(i)
                while num % i == 0:
                    num = num // i
            else:
                i += 1
        if num > 1:
            factors.add(num)
        return factors
    for i in range(len(nums)):
        ranges.append([])
        prime_scores.append(len(findPrimeFactors(nums[i])))
        heapq.heappush(heap,(-nums[i],i))
    q=[(prime_scores[0],0)]
    ranges[0].append(0)
    for i in range(1,len(prime_scores)):
        if prime_scores[i]<=q[-1][0]:
            ranges[i].append(i)
            q.append((prime_scores[i],i))
        else:
            while len(q) and q[-1][0]<prime_scores[i]:
                prime_score,index=q.pop()
                ranges[index].append(i-1)
            if len(q):
                ranges[i].append(q[-1][1]+1)
            else:
                ranges[i].append(0)
            q.append((prime_scores[i],i))
    if len(q):
        end_value=q[-1][1]
        while len(q):
            curr_value,curr_index=q.pop()
            ranges[curr_index].append(end_value)
    while k:
        MOD = 10**9 + 7
        curr_value,curr_index=heapq.heappop(heap)
        ways=(ranges[curr_index][1]-ranges[curr_index][0]+1+(ranges[curr_index][1]-curr_index)*(curr_index-ranges[curr_index][0]))
        if ways>=k:
            result = result * pow(-curr_value, k, MOD) % MOD
            return result
        else:
            result = result * pow(-curr_value, ways, MOD) % MOD
            k -= ways
    return result
print(maximumScore([8,3,9,3,8],2)) #O/P -> 81