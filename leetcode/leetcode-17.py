class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],
               "6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z'] }
        answer=[]
        
        if not digits: return [] 
        
        def dfs(i,word):
            if i==len(digits):
                answer.append(word)
                return
            for j in phone[digits[i]]:
                dfs(i+1,word +j)
        
        dfs(0,"")
        
        return answer