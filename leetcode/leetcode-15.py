class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer=[]
        for i in range(len(nums)-2):
            left, right =i+1, len(nums)-1
            while  left<right:
                if nums[left]+ nums[right]<-1*nums[i]:
                    left+=1
                elif nums[left] + nums[right]>-1*nums[i]:
                    right -=1
                else:
                    a=sorted([nums[i],nums[left],nums[right]])
                    if(a not in answer):
                        answer.append(a)
                    left+=1
                    right-=1
        return answer