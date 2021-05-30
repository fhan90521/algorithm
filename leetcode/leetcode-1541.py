class Solution:
    def minInsertions(self, s: str) -> int:
        answer = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append("(")
                i += 1
            else:
                if i < len(s) - 1 and s[i + 1] == ")":
                    i += 2
                else:  
                    i += 1
                    answer += 1
                if stack :
                    stack.pop()
                else:
                    answer+=1
        
        
        answer += len(stack) * 2
        
        return answer