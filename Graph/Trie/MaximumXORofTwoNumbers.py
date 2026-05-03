# You are given an integer array nums.
#
# Return the maximum XOR value of any two numbers in nums.
#
# ex:
# nums = [3,10,5,25,2,8]
# O/P -> 28
#
# Explanation:
# - 5 XOR 25 = 28, which is the maximum possible XOR.
#
# Idea:
# - Use a binary Trie to store numbers bit by bit.
# - For each number, try to pair it with another number that has opposite bits.
# - Opposite bits give XOR value 1, which helps maximize the result.
# - Check bits from most significant to least significant.
# - Insert each number into the Trie.
# - While searching, greedily choose the opposite bit if possible.
# - Keep track of the maximum XOR found.

def findMaximumXOR(nums):
    root = {}
    def insert(num):
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]
    def get_max_xor(num):
        node = root
        xor_value = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite = 1 - bit
            if opposite in node:
                xor_value |= (1 << i)
                node = node[opposite]
            else:
                node = node[bit]
        return xor_value
    for num in nums:
        insert(num)
    ans = 0
    for num in nums:
        ans = max(ans, get_max_xor(num))
    return ans
print(findMaximumXOR([3,10,5,25,2,8])) #O/P ->28