class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        k=0
        answer=0
        if(len(tokens)==1): return tokens[0]
        for i in range(len(tokens)):
            
            if(tokens[i].isdigit() or (tokens[i][0]=='-'and len(tokens[i])>1)):
                stack.append(tokens[i])
            else:
                    if(tokens[i]=="+"):
                        num1=int(stack.pop())
                        num2=int(stack.pop())
                        answer=num1+num2
                        stack.append(answer)
                        
                    if(tokens[i]=="/"):
                        num1=int(stack.pop())
                        num2=int(stack.pop())
                        answer=num2//num1
                        if(answer<0 and num2%num1!=0): answer+=1
                        stack.append(answer)
                    if(tokens[i]=="*"):
                        num1=int(stack.pop())
                        num2=int(stack.pop())
                        answer=num1*num2
                        stack.append(answer)
                    if(tokens[i]=="-"):
                        num1=int(stack.pop())
                        num2=int(stack.pop())
                        answer=num2-num1
                        stack.append(answer)
                
        return answer