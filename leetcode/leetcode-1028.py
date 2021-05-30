# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        preorder_input=collections.deque(S)
        preorder=collections.deque()
        deep=0
        while preorder_input:
            current=preorder_input.popleft()
            if(current!='-'):
                a=current
                while len(preorder_input)>=1 and preorder_input[0]!='-':   
                    current=preorder_input.popleft()
                    a+=current
                
                preorder.append([deep,a])
                deep=0
            else:
                deep+=1
        root_node=preorder.popleft()
        root=TreeNode(int(root_node[1]))
    
        def dfs(node,depth):
            
            if(preorder and node):
                current=preorder[0]
                if(node.left==None and current[0]==depth+1):
                    node.left=TreeNode(current[1])
                    preorder.popleft()
                dfs(node.left,depth+1)
                if(len(preorder)==0): return
                current=preorder[0]
                if(node.left and current[0]==depth+1):
                    node.right=TreeNode(current[1])
                    preorder.popleft()
                dfs(node.right,depth+1)
        dfs(root,0)
        return root