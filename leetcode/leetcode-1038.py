# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_val=0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if(root.right):
            self.bstToGst(root.right)
        self.sum_val+=root.val
        root.val=self.sum_val
        if(root.left):
            self.bstToGst(root.left)
        return root