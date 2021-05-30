class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse=True)
        current=intervals.pop()
        answer=[]
        answer.append(current)        
        while intervals:
            current=intervals.pop()
            prefer=answer[-1]
            if(prefer[1]>=current[0]):
                if(current[1]>prefer[1]):
                    prefer[1]=current[1]
            else:
                answer.append(current)
        
    
        
        return answer