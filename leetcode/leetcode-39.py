class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        
        def dfs(each,start):
            if(sum(each)>=target):
                if(sum(each)==target):
                    answer.append(each[:])
                return
            for i in range(start,len(candidates)):
                each.append(candidates[i])
                dfs(each,i)
                each.pop()
        dfs([],0)
        return answer 