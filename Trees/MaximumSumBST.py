# Given the root of a binary tree, return the maximum sum of all keys of any subtree which is also a Binary Search Tree (BST).
# A BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# ex:- root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]; O/P -> 20
#
#        1                      1 (null node) -> True; for left range - [node.val,node.val-1]; right range - [node.val+1,node.val]
#       / \                     To check whether current node is BST we use max value of left subtree and min value of right subtree
#      4   3                    however when we need to pass this information to above node we interchange the needed values to
#     / \ / \                       minimum of left tree and maximum of right tree which is found at left[0] and right[1]
#    2  4 2  5                      we check right[0] for current node but pass right[1] as this becomes the inner right node 
#           / \                     for the above subtree
#          4   6

from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max=[0]
        self.findMaxSums(root,max)
        return max[0]

    def findMaxSums(self,node,max):
        if not node.left and not node.right:
            if node.val > max[0]:
                max[0]=node.val
            return [node.val,node.val,node.val,True]
        left,right=[[node.val,node.val-1,0,True],[node.val+1,node.val,0,True]]
        valid_subtree=False
        temp_result=0
        if node.left:
            left = self.findMaxSums(node.left,max)
        if node.right:
            right = self.findMaxSums(node.right,max)
        if left[1]<node.val and right[0] > node.val and left[3] and right[3]:
            valid_subtree=True
            temp_result=node.val+left[2]+right[2]
            if max[0]< temp_result:
                max[0]=temp_result
        return [left[0],right[1],temp_result,valid_subtree]

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.left = TreeNode(2)
root.right.right = TreeNode(5)

root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(6)

print(sol.maxSumBST(root))  # O/P -> 20

