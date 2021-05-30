class Solution:
    def climbStairs(self, n: int) -> int:    
        pibo=[1]*(n+2)
        pibo[2]=2
        
        for i in range(3,n+1):
            pibo[i]=pibo[i-1]+pibo[i-2]
        return pibo[n]