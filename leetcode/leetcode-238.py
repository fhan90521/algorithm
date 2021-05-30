class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output=[]
        total=1
        for i in nums:
            output.append(total)
            total*=i
        total=1    
        for i in range(len(output)-1,-1,-1):
            output[i]*=total
            total*=nums[i]
        return output