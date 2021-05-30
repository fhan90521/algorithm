class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum=0
        for i in range(len(nums)):
            if(i%2==0):
                sum+=nums[i]
        return sum