# You are given nums and queries.
# Each query is [x, m].
#
# For each query, return the maximum XOR of x with any number in nums
# that is <= m.
# If no such number exists, return -1.
#
# ex:
# nums = [0,1,2,3,4]
# queries = [[3,1],[1,3],[5,6]]
# O/P -> [3,3,7]
#
# Idea:
# - Sort nums.
# - Sort queries by m, while keeping original query index.
# - Use a binary Trie to store numbers from nums.
# - For each query [x, m]:
#   - Add all nums <= m into the Trie.
#   - If Trie is empty, answer is -1.
#   - Otherwise, greedily search the Trie for the number that maximizes x XOR num.
# - Store the answer at the query's original index.

def maximizeXor(nums, queries):
    value_root={}
    sorted_queries=sorted([(i,q) for i,q in enumerate(queries)],key=lambda x: x[1][1])
    nums.sort()
    ans=[]
    j=0
    for query in sorted_queries:
        index=query[0]
        limit=query[1][1]
        num=query[1][0]
        while j < len(nums) and nums[j]<=limit:
            node_2=value_root
            for i in range(31,-1,-1):
                digit=(nums[j]>>i) & 1
                if digit in node_2:
                    node_2=node_2[digit]
                else:
                    node_2[digit]={}
                    node_2=node_2[digit]
            j+=1
        if not value_root:
            ans.append((-1, index))
            continue
        result=0
        node=value_root
        for i in range(31,-1,-1):
            digit=(num>>i) &1
            opposite= 1-digit
            if opposite in node:
                result=result+2**i
                node=node[opposite]
            else:
                node=node[digit]
        ans.append((result,index))
    sorted_ans=[r for r, i in sorted(ans, key=lambda x: x[1])]
    return sorted_ans
print(maximizeXor([0,1,2,3,4],[[3,1],[1,3],[5,6]])) #O/P -> [3,3,7]