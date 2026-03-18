# Problem:- Given the root of a binary tree where each node represents the amount of money in a house, 
# return the maximum amount the thief can rob without robbing two directly-linked houses (parent and child) on the same night.
# ex:- root = [3,2,3,null,3,null,1] ; O/P -> 7
# Tree for: root = [3,2,3,null,3,null,1]

#        3                                         10000    [13040,8040]
#       / \                                         / \
#      2   3                        [5000,0]     5000  1   [2041,3040] 
#       \   \                                         / \
#        3   1                           [1000,0]  1000 200 [200,2040]
#                                                       / \
#                                          [40,0]     40  2000   [2000,0]
 
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.robans(root))

    def robans(self,node) -> list:
        if not node.left and not node.right:
            return [node.val,0]
        left,right=[[0,0],[0,0]]
        if node.left:
            left=self.robans(node.left)
        if node.right:
            right=self.robans(node.right)
        return [node.val+left[1]+right[1],max(left)+max(right)]

sol= Solution()
root = TreeNode(10000)
root.left = TreeNode(5000)
root.right = TreeNode(1)
root.right.left = TreeNode(1000)
root.right.right = TreeNode(200)
root.right.right.left = TreeNode(40)
root.right.right.right = TreeNode(2000)
print(sol.rob(root)) # O/P -> 13040