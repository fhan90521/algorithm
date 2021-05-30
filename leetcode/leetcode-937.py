class Solution(object):
    def reorderLogFiles(self, logs):
        a=[]
        num=[]
        word=[]
        for i in logs:
            a=i.split()
            if(a[1].isalpha()):
                word.append(i)
            else:
                num.append(i)
        temp=''
        for i in range(len(word)):
            for k in range(0,i):
                if(word[i].split()[1:]==word[k].split()[1:]):
                    if(word[i].split()[0]<word[k].split()[0]):
                        temp=word[k]
                        word[k]=word[i]
                        word[i]=temp
                if(word[i].split()[1:]<word[k].split()[1:]):
                    temp=word[k]
                    word[k]=word[i]
                    word[i]=temp
        return word+num