class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       
        
        answer=[]
        
        def dfs(each,start,k):
            if(len(each)==k):
                answer.append(each[:])
                return
            for i in range(start,n+1):
                each.append(i)
                dfs(each,i+1,k)
                each.pop()
               
                
        dfs([],1,k)
        return answer