class Solution:
    def getSum(self, a: int, b: int) -> int:
        or_=a|b
        if(or_==-1): return 0
        x_or=a^b
        and_=a & b
        
        and_=and_<<1
       
        while(True):
            
            x_or,and_=x_or^and_,x_or&and_
            and_=and_<<1
            
            if(and_==0): break
            if(and_>2048):
                return x_or & 0xfff
        return x_or