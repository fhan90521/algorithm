class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        answer=[]
        while left<right:
            if(numbers[left]+numbers[right]>target):
                right-=1
            elif(numbers[left]+numbers[right]<target):
                left+=1
            else:
                answer.append(left+1)
                answer.append(right+1)
                left+=1
                right-=1
        return answer