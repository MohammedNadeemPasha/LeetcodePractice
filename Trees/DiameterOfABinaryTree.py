# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in the tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# ex:- root = [1,2,3,4,5]; O/P -> 3    |    root = [1,2]; O/P -> 1
#        1                                                1
#       / \                                              /
#      2   3                                            2
#     / \
#    4   5
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result=[0]
        self.findMaxDiameter(root,result)
        return 0 if result[0]==0 else result[0]-1
    def findMaxDiameter(self,node,result):
        if not node.left and not node.right:
            return 1
        left,right=0,0
        if node.left:
            left=self.findMaxDiameter(node.left,result)
        if node.right:
            right=self.findMaxDiameter(node.right,result)
        if left+right+1>result[0]:
            result[0]=left+right+1
        return max(left,right)+1

sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(sol.diameterOfBinaryTree(root))  # O/P -> 3

root = TreeNode(1)
root.left = TreeNode(2)
print(sol.diameterOfBinaryTree(root))  # O/P -> 1