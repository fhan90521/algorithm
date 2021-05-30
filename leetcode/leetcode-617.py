# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        queue=[root1,root2]
        if(root1==None): return root2
        if(root2==None): return root1
        while queue:
            current1=queue.pop(0)
            current2=queue.pop(0)

            if(current2):
                current1.val+=current2.val
            if(current1.left and current2.left):
                queue.append(current1.left)
                queue.append(current2.left)
            if(current1.left==None and current2.left):
                current1.left=current2.left
                
            if(current1.right and current2.right):
                queue.append(current1.right)
                queue.append(current2.right)
            if(current1.right==None and current2.right):
                current1.right=current2.right
                
        return root1