# You are given an array nums of unique positive integers.
# Think of each number as a node in a graph.
# There is an undirected edge between two numbers if they share a common factor greater than 1.
#
# Return the size of the largest connected component in this graph.
#
# ex:-
# nums = [4,6,15,35]
# O/P -> 4
#
# Explanation:
# - 4 and 6 share factor 2
# - 6 and 15 share factor 3
# - 15 and 35 share factor 5
# So all numbers belong to the same connected component.
#
# Idea:
# - Use Union-Find (Disjoint Set Union) to group numbers that share factors.
# - For each number, find its factors greater than 1.
# - Union the number with each of its factors.
# - Numbers that share any common factor will become part of the same set.
# - Count the size of each connected component.
# - Return the maximum component size.

from collections import defaultdict
def largestComponentSize(nums):
    node_parent=list(range(len(nums)))
    seen=set()
    parent=defaultdict(int)
    def prime_factors(n):
        factors = []
        start = 2
        while start * start <= n:
            if n % start == 0:
                factors.append(start)
                n //= start
            else:
                start += 1
        if n > 1:
            factors.append(n)
        return factors
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        rootx=find(x)
        rooty=find(y)
        if rootx != rooty:
            parent[rootx]=rooty
    def findNode(x):
        if node_parent[x]!=x:
            node_parent[x]=findNode(node_parent[x])
        return node_parent[x]
    def unionNode(x,y):
        rootx=findNode(x)
        rooty=findNode(y)
        if rootx != rooty:
            node_parent[rootx]=rooty
    for i,num in enumerate(nums):
        factors=prime_factors(num)
        for factor in factors:
            if factor ==1 or factor ==0:
                continue
            if factor not in seen:
                seen.add(factor)
                parent[factor]=i
            else:
                if parent[factor]==i:
                    continue
                else:
                    unionNode(node_parent[i],node_parent[parent[factor]])
    seen_nodes=defaultdict(int)
    for i,num in enumerate(nums):
        findNode(i)
        seen_nodes[node_parent[i]]+=1
    max_node=1
    for nodes in seen_nodes:
        if seen_nodes[nodes]>max_node:
            max_node=seen_nodes[nodes]
    return max_node


