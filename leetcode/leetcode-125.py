class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha=[]
        sentance=s.upper()
        for word in sentance:
            if(word<='Z' and word>='A'):
                alpha.append(word)
            if(word<='9' and word>='0'):
                alpha.append(word)
        length=len(alpha)
        len_half=length//2
        ispalin=True
        for i in range(len_half):
            if(alpha[i]!=alpha[length-i-1]):
                ispalin=False   
        return ispalin