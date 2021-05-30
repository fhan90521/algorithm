# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root==None): return 0
        queue=[root]
        depth=0
        
        
        
        while queue:
            depth +=1
            for i in range(len(queue)):
                current=queue.pop(0)
                if(current.left):
                    queue.append(current.left)
                if(current.right):
                    queue.append(current.right)
            
        return depth