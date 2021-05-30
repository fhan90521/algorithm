
def read_data():
    f = open("free.inp", "r")
    num = int(f.readline().rstrip())
    work_list=[]
    for _ in range(num):
        work =list(map(int,f.readline().split()))
        work_list.append(work)
    f.close()
    return work_list


def process(work_list,last_day):
    answer=[]
    #answer[n][0]:total work_day  answer[n][1]:max_benefit of Nst day 
    for i in range(last_day+1):
        answer.append([0,0])
    
        
    for i in range(1,last_day+1):
        if i==work_list[-1][1]:
            end_day=i
            while work_list and i==work_list[-1][1]:
                current=work_list.pop()
                start_day=current[0]
                cost=current[2]
                if(answer[start_day-1][1]==0):
                    if(answer[end_day-1][1]<cost+answer[start_day-1][1] and answer[end_day][1]<=cost+answer[start_day-1][1]):
                        if(answer[end_day][1]==cost+answer[start_day-1][1]):
                            if(answer[end_day][0]>answer[start_day-1][0]+end_day-start_day+1):
                                answer[end_day][0]=answer[start_day-1][0]+end_day-start_day+1
                        else:
                            answer[end_day][0]=answer[start_day-1][0]+end_day-start_day+1
                            answer[end_day][1]=answer[start_day-1][1]+cost
                    else:
                        if(answer[end_day-1][1]==cost+answer[start_day-1][1] and answer[end_day][1]==0):
                            if(answer[end_day-1][0]>answer[start_day-1][0]+end_day-start_day+1):
                                answer[end_day][0]=answer[start_day-1][0]+end_day-start_day+1
                                answer[end_day][1]=answer[end_day-1][1]
                        if(answer[end_day][1]==0):
                            answer[i]=answer[i-1][:]     
                else:
                    if(answer[end_day-1][1]<cost+answer[start_day-1][1]-10 and answer[end_day][1]<=cost+answer[start_day-1][1]-10 ):
                        if(answer[end_day][1]==cost+answer[start_day-1][1]-10):
                            if(answer[end_day][0]>answer[start_day-1][0]+end_day-start_day+1):
                                answer[end_day][0]=answer[start_day-1][0]+end_day-start_day+1
                        else:
                            answer[end_day][0]=answer[start_day-1][0]+end_day-start_day+1
                            answer[end_day][1]=answer[start_day-1][1]+cost-10
                    else:
                        
                        if(answer[end_day-1][1]==cost+answer[start_day-1][1]-10 and answer[end_day][1]==0 ):
                            if(answer[end_day-1][0]>answer[start_day-1][0]+end_day-start_day+1):
                                    answer[end_day][0]=answer[start_day-1][0]+end_day-start_day+1
                                    answer[end_day][1]=answer[end_day-1][1]
                        if(answer[end_day][1]==0):
                            answer[i]=answer[i-1][:]     
        else:
            answer[i]=answer[i-1][:]                   
        
    


    
    return answer


def print_data(data):
    f = open("free.out", "w")
    f.write(str(data[1]))
    f.write(' ')
    f.write(str(data[0])+"\n")
    f.close()


def main():
    work_list = read_data()
    work_list.sort(key= lambda x: x[1],reverse=True)
    answer=process(work_list,work_list[0][1])
    print_data(answer[-1])
    

if __name__== "__main__":
    main()