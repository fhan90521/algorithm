class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts=collections.Counter(tasks)
        keys=[]
        for i in counts:
            keys.append(i)
        result=0
        last=0
        while keys:
              
            if(len(keys)>=n+1):
                most=counts.most_common(n+1)
                result+=n+1
                for i in most:
                    counts[i[0]]-=1
                    
            else:
                result+=n+1
                last=n+1-len(keys)
                for i in counts:
                    counts[i]-=1

            for i in counts:
                if(counts[i]==0 and i in keys):
                    keys.remove(i)
                    
                    
            
        
        return result-last