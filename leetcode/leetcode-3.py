class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used={}
        maxlen=0
        start=0
        for index,alpha in enumerate(s):
            if(alpha in used and start<=used[alpha]):
                start=used[alpha]+1
            else:
                maxlen=max(maxlen,index-start+1)
            used[alpha]=index
        return maxlen