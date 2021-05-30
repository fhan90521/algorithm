class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        sentance=paragraph.lower()
        for i in sentance:
            if(not i.isalpha()):
                sentance=sentance.replace(i,' ')
        word=sentance.split()
        for i in word:
            if i in banned:
                word.remove(i)
        count=collections.Counter(word)
        most=count.most_common(1)
        return most[0][0]