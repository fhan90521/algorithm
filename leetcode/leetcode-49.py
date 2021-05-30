class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words=[]
        for word in strs:
            letters=[]
            for letter in word:
                letters.append(letter)
            letters.sort()
            words.append(letters)    
        anagrams=[]
        num=[]
        for i in range(len(strs)):
            group=[]
            if(i not in num):
                group.append(strs[i])
                num.append(i)
            for k in range(len(strs)):
                if(words[i]==words[k] and k not in num):
                    group.append(strs[k])
                    num.append(k)
            if(len(group)!=0):
                anagrams.append(group)
        return anagrams