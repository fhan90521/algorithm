class Solution:
    def fib(self, n: int) -> int:
        if(n==0): return 0
        pibo=[0]*(n+1)
        pibo[1]=1
        for i in range(2,n+1):
            pibo[i]=pibo[i-1]+pibo[i-2]
        return pibo[n]