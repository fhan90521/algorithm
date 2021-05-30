class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = collections.Counter(stones)
        sum_counts=0
        for i in jewels:
            if(i in counts):
                sum_counts+=counts[i]
        return sum_counts