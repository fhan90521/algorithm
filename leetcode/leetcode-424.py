class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts=collections.defaultdict(int)
        
        
        result = 0
        left = 0
        right = 0
        num_count = k
        
        while right < len(s)-1:
           
            while num_count >= 0 :
                counts[s[right]] += 1
                right += 1
                if right==len(s) : 
                    num_count -=1 
                    break
                if s[right] != s[left]:
                    num_count -= 1
           
            
            
            
            if right-left+num_count+1 > result:
                result = right-left+num_count+1
                if(result>len(s)): return len(s)      
            
            
            
            while (right-left) - counts[s[left]] >= k and left<right:
                
                counts[s[left]] -= 1
                left += 1
                if left==len(s)-1 : break

            if(left==right):
                num_count=k
            else:
                num_count = k - ((right-left+1) - counts[s[left]])
            if right-left+num_count+1 > result:
                result = right-left+num_count+1
                if(result>len(s)): return len(s)      
            
            
            
        return result