class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        Mask=0xFF
        
        while data:
            current=data.pop(0)
            current_bin=bin(current)[2:].zfill(8)
           
            if(current_bin[:2]!='10'):
                num=0
                for i in current_bin:
                    if(i=='1'):
                        num+=1
                    else:
                        break
                if(num>4): return False
                if(num==0):
                    continue
                else:
                    num-=1
                    for i in range(num):
                        if(data):
                            current=data.pop(0)
                            current_bin=bin(current)[2:].zfill(8)
                            if(current_bin[:2]!='10'):
                                return False
                        else:
                            return False
            else: return False
        return True