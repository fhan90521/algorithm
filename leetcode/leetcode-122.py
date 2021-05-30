class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev=0
        current=1
        result=0
        while current<len(prices):
            if(prices[current]-prices[prev]>0):
                result+=prices[current]-prices[prev]
            current+=1
            prev+=1
        return result
        