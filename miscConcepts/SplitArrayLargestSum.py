# You are given nums and an integer k.
#
# Split nums into k non-empty continuous subarrays. Return the minimum possible largest subarray sum.
#
# ex:
# nums = [7,2,5,10,8], ex ->  Best split is [7,2,5] and [10,8].
# k = 2
# O/P -> 18
#
# Idea:
# - Use binary search on the answer.
# - The minimum possible answer is max(nums).
# - The maximum possible answer is sum(nums).
# - For a guessed max sum mid:
#   - Greedily split nums into subarrays where each sum <= mid.
#   - Count how many subarrays are needed.
# - If needed subarrays <= k:
#   - mid is valid, try smaller.
# - Else:
#   - mid is too small, try larger.
# - Return the smallest valid max sum.
def splitArray(nums, k):
    left=0
    right=0
    ans=float('inf')
    for i in nums:
        right+=i
        left=max(left,i)
    while left<=right:
        mid_sum=int((left+right)/2)
        count=1
        _sum=0
        prev_sum=0
        for i in nums:
            if _sum + i <=mid_sum:
                _sum+=i
            else:
                prev_sum=max(prev_sum,_sum)
                _sum=i
                count+=1
        prev_sum=max(prev_sum,_sum)
        if count <=k:
            ans=min(ans,prev_sum)
            right=mid_sum-1
        else :
            left=mid_sum+1
    return ans
print(splitArray([7,2,5,10,8],2)) # O/P -> 18