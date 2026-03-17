# Given the root of a binary tree where each node has an integer value,
# return the maximum path sum of any non-empty path.
# A path is a sequence of connected nodes and does not need to pass through the root.
# Each node can appear at most once in the path.
# The path sum is the sum of the node values along the path.
# ex:- root = [-10,9,20,null,null,15,7]; O/P -> 42
# Intuition - (max of (node value,node value+left subtree max value+right subtree max value) to be taken to previous level for further possible
#              maximum path sum) &&& sum(node value+ left subtree max+ right subtree max) (This path could be the maximum path)

#        -10                                                                       10    [max(10,(6)10-4,(7)10-3),|3(10-4-3)]
#       /   \                                                                     /  \     
#      9     20            [max(-8,(-4)-8+4,(-5)-8+3)),|-1(-8+4+3)]=[-4,|-1]    -8   -5   [max(-5,(-3)-5+2,(-4)-5+1)),|-2(-5+2+1)] = [-3,|-2]
#           /  \                                                                / \  / \
#         15    7                                                              4  3  2  1    
#                                                                         [4,4][3,3][2,2][1,1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result=[float('-inf')]
        temp_res=self.dpMaxPath(root,result)
        return max(temp_res[0],result[0])
    def dpMaxPath(self,node,result) -> list:
        if not node.left and not node.right:
            if result[0]<node.val:
                result[0]=node.val
            return [node.val,node.val]
        left,right=[[0,0],[0,0]]
        if node.left:
            left=self.dpMaxPath(node.left,result)
        if node.right:
            right=self.dpMaxPath(node.right,result)
        temp=[max(node.val,node.val+left[0],node.val+right[0]),node.val+left[0]+right[0]]
        if result[0]<max(temp):
            result[0]=max(temp)
        return temp

sol= Solution()
root = TreeNode(10,             #(2) ex -> O/P -> 10
        TreeNode(-8,
            TreeNode(4),
            TreeNode(3)
        ),
        TreeNode(-5,
            TreeNode(2),
            TreeNode(1)
        )
)
print(sol.maxPathSum(root))