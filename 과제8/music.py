import collections

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


def main():
    score,string = read_data()
    
    match=score[0]
    mismatch=score[1]
    gap=score[2]
    length=len(string)+1
    table=[]
    start_table=collections.defaultdict(set)
    
    for i in range(length):
        table.append([0]*length)
    for i in range(length):
        start_table[(0,i)].add((0,i))
        start_table[(i,0)].add((i,0))
    max_score=0
    result=[(10000000,10000000),(10000000,10000000)]
    for i in range(1,length):
        for j in range(1,length):
                if(i<=j):
                    if(string[i-1]==string[j-1]):
                        match_point=match
                    else:
                        match_point=mismatch
                    left=0
                    leftup=0
                    up=0
                    for start_point in start_table[(i,j-1)]:
                        if(start_point[1]+1>i and table[i][j]<table[i][j-1]+gap):
                            table[i][j]=table[i][j-1]+gap
                            left=1  
                    for start_point in start_table[(i-1,j)]:
                        if(start_point[1]+1>i and table[i][j]<table[i-1][j]+gap):
                            table[i][j]=table[i-1][j]+gap
                            up=1
                    for start_point in start_table[(i-1,j-1)]:
                        if(start_point[1]+1>i and table[i][j]<table[i-1][j-1]+match_point):
                            table[i][j]=table[i-1][j-1]+match_point
                            leftup=1
                    
                    if( table[i][j]==0 ): start_table[(i,j)].add((i,j))
                    if( table[i][j]==table[i][j-1]+gap):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i,j-1)])
                    if( table[i][j]==table[i-1][j]+gap):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i-1,j)])
                    if( table[i][j]==table[i-1][j-1]+match_point):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i-1,j-1)])
                    
                    
                    start_points=sorted(start_table[(i,j)])
            
                    if(max_score<=table[i][j]):
                        for start_point in start_points:
                            if(start_point[1]+1>i and max_score<table[i][j]):
                                max_score=table[i][j]
                                result=[(start_point[0],i-1),(start_point[1],j-1)]
                                break
                            elif(start_point[1]+1>i and max_score==table[i][j]):
                                if(result[0][0]>start_point[0]):
                                    result=[(start_point[0],i-1),(start_point[1],j-1)]
                                    break
                                else:
                                    if(result[0][0]==start_point[0] and result[1][0]>start_point[1]):
                                        result=[(start_point[0],i-1),(start_point[1],j-1)]  
                                        break
    table=[]
    start_table=collections.defaultdict(set)
    reverse_str=string[::-1]
    reverse=0
    for i in range(length):
        table.append([0]*length)
    for i in range(length):
        start_table[(0,i)].add((0,i))
        start_table[(i,0)].add((i,0))
    h=[(10000000,10000000),(10000000,10000000)]
    for i in range(1,length):
        for j in range(1,length):
                if(i<=j):
                    if(reverse_str[i-1]==reverse_str[j-1]):
                        match_point=match
                    else:
                        match_point=mismatch
                    left=0
                    leftup=0
                    up=0
                    for start_point in start_table[(i,j-1)]:
                        if(start_point[1]+1>i and table[i][j]<table[i][j-1]+gap):
                            table[i][j]=table[i][j-1]+gap
                            left=1  
                    for start_point in start_table[(i-1,j)]:
                        if(start_point[1]+1>i and table[i][j]<table[i-1][j]+gap):
                            table[i][j]=table[i-1][j]+gap
                            up=1
                    for start_point in start_table[(i-1,j-1)]:
                        if(start_point[1]+1>i and table[i][j]<table[i-1][j-1]+match_point):
                            table[i][j]=table[i-1][j-1]+match_point
                            leftup=1
                    
                    if( table[i][j]==0 ): start_table[(i,j)].add((i,j))
                    if( table[i][j]==table[i][j-1]+gap):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i,j-1)])
                    if( table[i][j]==table[i-1][j]+gap):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i-1,j)])
                    if( table[i][j]==table[i-1][j-1]+match_point):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i-1,j-1)])
                    
                    
                    start_points=sorted(start_table[(i,j)],reverse=True)
        
                    if(reverse<=table[i][j]):
                        for start_point in start_points:
                            if(start_point[1]+1>i and reverse<table[i][j]):
                                reverse=table[i][j]
                                reverse_result=[(start_point[0],i-1),(start_point[1],j-1)]
                                break
                            elif(start_point[1]+1>i and reverse==table[i][j]):
                                if(reverse_result[0][0]>start_point[0]):
                                    reverse_result=[(start_point[0],i-1),(start_point[1],j-1)]
                                    break
                                else:
                                    if(reverse_result[0][0]==start_point[0] and reverse_result[1][0]>start_point[1]):
                                        reverse_result=[(start_point[0],i-1),(start_point[1],j-1)]  
                                        break
    if(reverse<=max_score):
        
        print(result)
        print(string[result[0][0]:result[0][1]+1])
        print(string[result[1][0]:result[1][1]+1])
        print(max_score)
        result.sort()
        f = open("music.out", "w")
        f.write(string[result[0][0]:result[0][1]+1]+'\n')
        f.write(string[result[1][0]:result[1][1]+1]+'\n')
        f.write(str(max_score)+'\n')
        f.close()
    else:
        string1=reverse_str[reverse_result[0][0]:reverse_result[0][1]+1]
        string2=reverse_str[reverse_result[1][0]:reverse_result[1][1]+1]
        string1=string1[::-1]
        string2=string2[::-1]
        print(result)
        print(string2)
        print(string1)
        print(reverse)
        result.sort()
        f = open("music.out", "w")
        f.write(string2+'\n')
        f.write(string1+'\n')
        f.write(str(reverse)+'\n')
        f.close()

if __name__== "__main__":
    main()