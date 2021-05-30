# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if(nums):
            middle=len(nums)//2
            current=TreeNode(nums[middle])
            current.left=self.sortedArrayToBST(nums[:middle])
            current.right=self.sortedArrayToBST(nums[middle+1:])
            return current
        else: return