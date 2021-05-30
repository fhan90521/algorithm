class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=collections.Counter(nums)
        answer=counts.most_common(k)
        real_answer=[]
        for i in answer:
            real_answer.append(i[0])
        
        return real_answer