import collections
def read_data():
    f = open("jug.inp", "r")
    
    s=list(map(int,f.readline().rstrip().split()))
    input_data=[]
    while(True):
        num = f.readline().rstrip()
        if(not num):
            break
        input_data.append(int(num))
    f.close()
    return s,input_data


def process(s,input_data):
    who_win=[0]*101
    prev_dict=collections.defaultdict(list)
    
    for i in range(101):
        if(i<s[0]):
            who_win[i]=1
        else:
            for k in range(3):
                if((i-s[k]>=0 and len(prev_dict[i-s[k]])==1 and prev_dict[i-s[k]][0]==s[k]) or( i-s[k]>=0 and who_win[i-s[k]]==0)):
                        who_win[i]=1
                        prev_dict[i].append(s[k])
    
    answer=[]
    for i in input_data:
        if(who_win[i]==1):
            answer.append('F')
        else:
            answer.append('S')
    return answer


def print_data(answer):
    f = open("jug.out", "w")
    
    for i in answer:
        f.write(i+'\n')
    f.close()


def main():
    s,input_data = read_data()
    answer=process(s,input_data)
    print(answer)
    print_data(answer)

if __name__== "__main__":
    main()