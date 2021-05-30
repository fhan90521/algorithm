# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(root==None):return
        queue=[root]
        answer=[]
        
        while queue:
            current=queue.pop(0)
            if(current):
                queue.append(current.left)
                queue.append(current.right)
                answer.append(current.val)
            else:
                answer.append(None)
        return answer
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(data==None):return
        val=data.pop(0)
        root=TreeNode(val)
        queue=[root]
        while queue:
            current=queue.pop(0)
            if(data):
                val=data.pop(0)
                if(val!=None):
                    current.left=TreeNode(val)
                    queue.append(current.left)
            if(data):
                val=data.pop(0)
                if(val!=None):
                    current.right=TreeNode(val)
                    queue.append(current.right)
        return root    
                
                        
            
                
            
            
     
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))