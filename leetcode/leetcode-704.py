class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        index=len(nums)//2
        right=len(nums)
        left=0
        while(True):
            
            if(nums[index]==target):
                return index
            elif(nums[index-1]==target):
                return index-1
            else:
                if(index==0 or index==right-1):
                    return -1
                if(nums[index]<target):
                    index=(index+right)//2
                else:
                    right=index
                    index=index//2