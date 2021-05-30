import collections
def read_data():
    f = open("1.inp", "r")
    
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
    result=[(100,100),(100,100)]
    for i in range(1,length):
        for j in range(1,length):
            if(i<=j):
                if(string[i-1]==string[j-1]):
                    match_point=match
                else:
                    match_point=mismatch
                max_point=max(0,table[i][j-1]+gap,table[i-1][j]+gap,table[i-1][j-1]+match_point)
                table[i][j]=max_point
                if(max_point==0): start_table[(i,j)].add((i,j))

                else:
                    if(max_point==table[i][j-1]+gap):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i,j-1)])
                    if(max_point==table[i-1][j]+gap):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i-1,j)])
                    if(max_point==table[i-1][j-1]+match_point):start_table[(i,j)]=start_table[(i,j)].union(start_table[(i-1,j-1)])
                print(start_table[(i,j)])
                for start_point in start_table[(i,j)]:
                    if(start_point[1]+1>i and max_score<=max_point):
                        if(max_score<max_point):
                            max_score=max_point
                            result=[(start_point[0],i-1),(start_point[1],j-1)]
                        elif(max_score==max_point):
                            if(result[0][0]>start_point[0]):
                               result=[(start_point[0],i-1),(start_point[1],j-1)] 
                            else:
                                if(result[0][0]==start_point[0] and result[1][0]>start_point[1]):
                                    result=[(start_point[0],i-1),(start_point[1],j-1)] 
    f = open("music.out", "w")
    f.write(string[result[0][0]:result[0][1]+1]+'\n')
    f.write(string[result[1][0]:result[1][1]+1]+'\n')
    f.write(str(max_score)+'\n')
    f.close()
if __name__== "__main__":
    main()