import collections
import itertools


def read_data():
    f = open("3.inp", "r")
    N=int(f.readline())
    down=list(map(int,f.readline().rstrip().split()))
    right=list(map(int,f.readline().rstrip().split()))
    right_down=list(map(int,f.readline().rstrip().split()))
    left_down=list(map(int,f.readline().rstrip().split()))
    return N,down,right,right_down,left_down


def process(costs,edges):
    pass



def main():
    N,down,right,right_down,left_down = read_data()
    stack=[]
    stack_down=[0]*N
    stack_right_down=[0]*(2*N-1)
    stack_left_down=[0]*(2*N-1) 
    answer=[]
    combi=[]
    a=itertools.combinations(range(N),4)
    print(a)
    for i in range(N):
        combi.append(list(itertools.combinations(range(N),right[i])))
    
    def check(sero,garo):
        if(stack_down[garo]+1>down[garo]):
            return False
        if(stack_left_down[garo+sero]+1>left_down[garo+sero]):
            return False
        if(stack_right_down[((N-1)-garo)+sero]+1>right_down[((N-1)-garo)+sero]):
            return False
        return True
    def dfs(sero):
        
        if(answer):
            return
        if(sero==N):
            answer.append(stack[:])
            return
        for line in combi[sero]:
            flag=True
            for garo in line:
                if(not check(sero,garo)):
                    flag=False
                    break
            if(flag):        
                stack.append(line)
                for garo in line:
                    stack_down[garo]+=1
                    stack_left_down[garo+sero]+=1
                    stack_right_down[((N-1)-garo)+sero]+=1
                dfs(sero+1)
                for garo in line:
                    stack_down[garo]-=1
                    stack_left_down[garo+sero]-=1
                    stack_right_down[((N-1)-garo)+sero]-=1
                stack.pop()
    dfs(0)
    board=[]
    for _ in range(N):
        board.append(['-']*N)
    for i in range(N):
        for k in answer[0][i]:
            board[i][k]='B'
    

    f = open("ct.out", "w")
    for i in range(N):
        for k in range(N):
            f.write(board[i][k])
            f.write(" ")
        f.write("\n")
    
    

if __name__== "__main__":
    main()