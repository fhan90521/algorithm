class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[0]
        days=[]
        for _ in range(len(T)):
            days.append(0)
        for i in range(1,len(T)):
            while(stack and T[stack[-1]]<T[i] ):
                days[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return days    