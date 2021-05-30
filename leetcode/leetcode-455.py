class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        
        s.sort(reverse=True)
        result=0
        while g and s:
            current=g.pop()
            while True:
                if(s):
                    s_current=s.pop()
                    if(s_current>=current):
                        result+=1 
                        break
                else:break
        
        return result