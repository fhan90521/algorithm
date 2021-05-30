# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isTrue=True
    def isBalanced(self, root: TreeNode) -> bool:
        if(root==None):
            return 1
        left_height=self.isBalanced(root.left)
        right_height=self.isBalanced(root.right)
        if(abs(left_height-right_height)>=2):
            self.isTrue=False
        if(not self.isTrue):
            return False
        return max(left_height,right_height)+1