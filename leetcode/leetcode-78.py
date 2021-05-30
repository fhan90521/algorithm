class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        def dfs(each,start):
            answer.append(each)
            for i in range(start,len(nums)):
                
                dfs(each+[nums[i]],i+1)
            
        dfs([],0)
        return answer