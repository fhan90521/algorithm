
def read_data():
    f = open("music.inp", "r")
    
    score=list(map(int,f.readline().rstrip().split()))
    string = f.readline().rstrip()

    return score,string


def process(s,input_data):
    return 0

def print_data(answer):
    f = open("jug.out", "w")
    
    for i in answer:
        f.write(i+'\n')
    f.close()

def backtrace(end_point,table,prev):
    sero=end_point[0]
    garo=end_point[1]
    while(1):
        if(prev[sero][garo]==None):
            break
        if (prev[sero][garo]=="leftup") :
            sero-=1
            garo-=1
        
    
        elif (prev[sero][garo]== "left"):
            garo-=1
        
        elif (prev[sero][garo]== "up"):
            sero-=1
        
        
    return (sero,garo)
def main():
    score,string = read_data()
    
    match=score[0]
    mismatch=score[1]
    gap=score[2]
    max_score=0
    
    result=[(100000000000,10000000000),(100000000000,10000000000)]
    for i in range(1,len(string)):
        left_str=string[:i]
        right_str=string[i:]
        sero=len(left_str)+1
        garo=len(right_str)+1
        table=[]
        prev=[]     
        prev_max=max_score
        jonjae=0
        for j in range(sero):
            table.append(garo*[0])
            prev.append(garo*[None])
        end_point=0
        for j in range(1,sero):
            for k in range(1,garo):
                
                if(left_str[j-1]==right_str[k-1]):
                    match_point=match
                else:
                    match_point=mismatch
                left=table[j][k-1]+gap
                up=table[j-1][k]+gap
                leftup=table[j-1][k-1]+match_point
                
                if (leftup <= 0 and up <= 0 and left <= 0):
                    table[j][k] = 0
                    prev[j][k]= None 
                    continue
                if (leftup >= up):
                    if (leftup >= left):
                        table[j][k] = leftup
                        prev[j][k]= "leftup" 
                    
                    else:
                        table[j][k] = left
                        prev[j][k]= "left" 
                    
                else:
                    if (up>= left):
                        table[j][k] = up
                        prev[j][k]= "up"
                    
                    else:
                        table[j][k] = left
                        prev[j][k]= "left"
                if(max_score<table[j][k] ):
                    max_score=table[j][k]
                    end_point=(j,k)
        
        if(end_point!=0):
            start_point=backtrace(end_point,table,prev)     
            result=[(start_point[0],end_point[0]),(start_point[1]+i,end_point[1]+i)]
            
                       
        
    print(result)          
    print(string[result[0][0]:result[0][1]])
    print(string[result[1][0]:result[1][1]])
    print(max_score)    
    f = open("music.out", "w")
    f.write(string[result[0][0]:result[0][1]]+'\n')
    f.write(string[result[1][0]:result[1][1]]+'\n')
    f.write(str(max_score)+'\n')
    f.close()
    
    
    
if __name__== "__main__":
    main()
