class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer=[]
        heap=[]
        if(k==1):return nums
        for index,value in enumerate(nums[:k]):
            heapq.heappush(heap,(-value,index))
        answer.append(heap[0][0]*-1)
        left=1
        right=k
        for index,value in enumerate(nums):
            if(index>=k):
                heapq.heappush(heap,(-value,index))
                while(heap[0][1]>right or heap[0][1]<left):
                    heapq.heappop(heap)
                
                answer.append(heap[0][0]*-1)
                
                left+=1
                right+=1
        return answer