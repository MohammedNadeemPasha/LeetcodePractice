# Given the root of a binary tree where each node has an integer value,return the length of the longest path where all nodes 
# in the path have the same value. A path is a sequence of connected nodes and does not need to pass through the root.
# Each node can appear at most once in the path. The length of the path is the number of edges between the nodes.
# ex:- root = [5,4,5,1,1,null,5]; O/P -> 2    |    root = [1,4,5,4,4,null,5] ; O/P -> 2
#        5                                                  1
#       / \                                                / \
#      4   5                                              4   5
#     / \   \                                            / \   \
#    1   1   5                                          4   4   5
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        longest=[0]
        self.longestPath(root,longest)
        return 0 if longest[0] == 0 else longest[0] - 1

    def longestPath(self,node,longest)-> list:
        if not node.left and not node.right:
            return [node.val,1]
        left,right=[[0,0],[0,0]]
        left_max,right_max=[0,0]
        if node.left:
            left = self.longestPath(node.left,longest)
        if node.right:
            right = self.longestPath(node.right,longest)
        if node.val == left[0]:
            left_max = left[1]
        if node.val == right[0]:
            right_max= right[1]
        if longest[0] < 1+left_max+right_max:
            longest[0]=1+left_max+right_max
        return [node.val,1+max(left_max,right_max)]

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)
print(sol.longestUnivaluePath(root))  #O/P -> 2

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
print(sol.longestUnivaluePath(root))  # O/P -> 2