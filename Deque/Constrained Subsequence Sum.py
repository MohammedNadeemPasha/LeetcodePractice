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
            print(dq)
            if dq[-1][1] + nums[i] > dq[-1][1]:
                dq[-1][0].append(nums[i])
                dq[-1][1] += nums[i]
                i += 1
            else:
                if nums[i] > dq[-1][1] + nums[i]:
                    dq.pop()
                    dq.append([[nums[i]], nums[i]])
                    i += 1
                else:
                    skip = k
                    ref=dq[-1]
                    curr_list = []

                    while skip > 0:
                        temp = copy.deepcopy(ref[0])
                        print(temp)
                        temp_sum = ref[1] + nums[i]

                        while len(curr_list) and curr_list[-1][1] < temp_sum:
                            curr_list.pop()

                        curr_list.append([temp.append(nums[i]), temp_sum])
                        print(curr_list)
                        skip -= 1
                        i += 1

                    dq.append(curr_list[0])

            while len(dq) >= 2 and dq[-1][1] > dq[-2][1]:
                del dq[-2]

            return dq[0][0]


nums = [10, -2, -10, -5, 20]
k = 2

s = Solution()
print(s.constrainedSubsetSum(nums, k))