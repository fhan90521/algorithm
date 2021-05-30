class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=set()
        nums=set(nums2)
        for num in nums1:
            if(num in nums):
                answer.add(num)
        return answer