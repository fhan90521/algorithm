class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s)%2==1): return False
        left=[]
        is_true=True
        for i in s:
            if( (i==')' or i==']' or i=='}') and len(left)==0): 
                is_true=False
                break
            if(i=='(' or i=='[' or i=='{'):
                left.append(i)
                continue
            if(i==')' and left.pop()!='('):
                is_true=False
                break
            if(i=='}' and left.pop()!='{'):
                is_true=False
                break
            if(i==']' and left.pop()!='['):
                is_true=False
                break
        if(len(left)>0):is_true=False
        return is_true
        