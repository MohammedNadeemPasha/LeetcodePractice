# Serialization is the process of converting a data structure or object into a sequence of bits 
# so that it can be stored in a file or memory buffer, or transmitted across a network connection 
# to be reconstructed later in the same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. 
# 
# ex:- root = [1,2,3,null,null,4,5]; serialized -> "1,2,null,null,3,4,null,null,5,null,null"
#
#        1
#       / \          (IMP - CHECK INORDER TRAVERSAL BASED SOLUTION BELOW)
#      2   3
#         / \
#        4   5

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return ""
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        if node:
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            res.append("#")
    return ",".join(res)

def deserialize(data):
    if not data:
        return None
    vals = data.split(",")
    root = TreeNode(int(vals[0]))
    q = deque([root])
    i = 1
    while q:
        node = q.popleft()
        if vals[i] != "#":
            node.left = TreeNode(int(vals[i]))
            q.append(node.left)
        i += 1
        if vals[i] != "#":
            node.right = TreeNode(int(vals[i]))
            q.append(node.right)
        i += 1
    return root



# Serializing and deserializing a tree using dfs approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:

#     def serialize(self, root):
#         vals = []

#         def dfs(node):
#             if not node:
#                 vals.append('#')
#                 return
#             vals.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)

#         dfs(root)
#         return ','.join(vals)

#     def deserialize(self, data):
#         vals = iter(data.split(','))

#         def dfs():
#             v = next(vals)
#             if v == '#':
#                 return None

#             node = TreeNode(int(v))
#             node.left = dfs()
#             node.right = dfs()
#             return node

#         return dfs() 