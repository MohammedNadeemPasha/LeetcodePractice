from collections import deque
import copy
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        result = []
        curr_arr = []
        dq = deque()
        i = 1

        dq.append([[nums[0]], nums[0]])

        while  i < len(nums):
            print(f'dq-{dq}\n i-{i}')
            if dq[-1][1] + nums[i] > dq[-1][1] and dq[-1][1] + nums[i] > nums[i]:
                dq[-1][0].append(nums[i])
                dq[-1][1] += nums[i]
                i += 1
            else:
                if nums[i] > dq[-1][1] + nums[i]:
                    dq.append([[nums[i]], nums[i]])
                    i += 1
                else:
                    skip = k
                    ref=dq[-1]
                    curr_list = []

                    while skip > 0 and i<len(nums):
                        temp = copy.deepcopy(ref[0])
                        temp_sum = ref[1] + nums[i]
                        while len(curr_list) and curr_list[-1][1] <= temp_sum:
                            curr_list.pop()
                        temp.append(nums[i])
                        curr_list.append([temp, temp_sum,i])
                        print(curr_list)
                        skip -= 1
                        i += 1
                        if(temp_sum>ref[1]):
                          break

                    dq.append([curr_list[0][0],curr_list[0][1]])
                    i=curr_list[0][2]+1
            while len(dq) >= 2 and dq[-1][1] > dq[-2][1]:
                del dq[-2]
        return dq[0][1]


nums = [100,-10,-10,-10,-2,-2,-10,-100,15,-5,-10,10,2,-10,5,20]
k = 2

s = Solution()
print(s.constrainedSubsetSum(nums, k))