class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=nums.index(min(nums))
        
        left=0
        right=len(nums)-1
        length=len(nums)
        while left<=right:
            mid=(left+right)//2
            if(nums[(mid+pivot)%length]<target):
                left=mid+1
            elif(nums[(mid+pivot)%length]>target):
                right=mid-1
            else:
                return (mid+pivot)%length
        return -1