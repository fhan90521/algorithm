class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=-1000000
        s=0
        for i in nums:
            s+=i
            if(s>max_sum):
                max_sum=s
            if(s<0):
                s=0
        return max_sum