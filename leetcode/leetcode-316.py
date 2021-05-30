class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        for index,alpha in enumerate(s): 
            while(stack and stack[-1]>alpha and alpha not in stack and stack[-1] in s[index:] ):
                stack.pop()     
            if(alpha not in stack):
                stack.append(alpha)   
        answer=''.join(stack)
        return answer