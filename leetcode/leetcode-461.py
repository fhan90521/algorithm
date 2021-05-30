class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result=bin(x^y)
        answer=0
        for i in result:
            if(i=='1'):
                answer+=1  
                
        return answer