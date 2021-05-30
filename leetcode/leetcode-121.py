class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_prices=prices[0]
        max_profit=0
        for i in prices:
            min_prices=min(min_prices,i)
            max_profit=max(max_profit,i-min_prices)
            
        return max_profit