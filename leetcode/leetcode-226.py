# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue=[root]
        if(root==None): return root
        while queue:
            current=queue.pop(0)
            if(current.left):
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)
            current.left,current.right=current.right,current.left
            
        return root