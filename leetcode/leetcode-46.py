class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        each=[]
        def dfs():
            if(len(each) == len(nums)):
                new=each[:]
                answer.append(new)
            for i in nums:
                if i not in each:
                    each.append(i)
                    dfs()
                    each.pop()
        dfs()
        return answer
                