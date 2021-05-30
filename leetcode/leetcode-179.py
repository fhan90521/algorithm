class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num=nums.pop()
        answer=[str(num)]
        while nums:
            left=answer[:]
            right=answer[:]
            num=nums.pop()
            current=list(str(num))
            length=len(answer)
            for i in range(length):
                
                answer_current=list(str(answer[i]))
                if(current[0]>=answer_current[0]):
                    left.insert(i,str(num))
                    right.insert(i+1,str(num))
                    left_num=''.join(left)
                    right_num=''.join(right)
                    
                    if(int(left_num)>int(right_num)):
                        answer.insert(i,str(num))
                        break
                    left=answer[:]
                    right=answer[:]
                    
                
                if(i==length-1):
                    answer.append(str(num))
            
        
        answer_num="".join(answer)
        if(int(answer_num)==0):return '0'
                
        return "".join(answer)
                            
                             