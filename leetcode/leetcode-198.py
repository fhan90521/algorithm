class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if(len(nums)>=3):
            sum_list=[nums[0],nums[1],nums[2]+nums[0]]
            for i in range(3,len(nums)):
                sum_list.append(max(sum_list[i-2]+nums[i],sum_list[i-3]+nums[i]))
            return max(sum_list)   
            
        else:
            if(len(nums)==1): return nums[0]
            if(len(nums)==2): return max(nums[0],nums[1])
            return max(nums[1],nums[0]+nums[2])
                    