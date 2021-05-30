import collections

def read_data():
    f = open("marathon.inp", "r")
    
    s=list(map(int,f.readline().rstrip().split()))
    edge_num=s[1]
    costs=collections.defaultdict(int)
    edges=collections.defaultdict(list)
    for i in range(edge_num):
        s=list(f.readline().rstrip().split())
        cost=int(s[2])
        left=s[0]
        right=s[1]
        edges[left].append(right)
        edges[right].append(left)
        costs[(left,right)]=cost
        costs[(right,left)]=cost
    return costs,edges


def process(costs,edges):
    answers=[]
    stack=['a']
    discovered=set('a')
    maxlen=[0]
    
    def dfs(current,total):
        total+=costs[(stack[-1],current)]
        stack.append(current)
        discovered.add(current)
        for vertex in edges[current]:
            if (vertex not in discovered and total+costs[(current,vertex)]<42):
                dfs(vertex,total)
                stack.pop()
                discovered.remove(vertex)    
            else:
                if(vertex == 'a' and total+costs[(current,vertex)]==42):
                    if(len(stack)>maxlen[0]):
                        maxlen[0]=len(stack)
                        answers.clear()
                        answers.append(stack[:])
                    else:
                        if(len(stack)==maxlen[0]):
                            answers.append(stack[:])

    edges['a'].sort()    
    for i in range(len(edges['a'])-1):
        dfs(edges['a'][i],0)
        stack.pop()
        discovered.remove(edges['a'][i])
        
        
    
    answers.sort()
    if(answers):
        answer=answers[0]
    else:
        answer="None"
    return answer




def main():
    costs,edges = read_data()
    answer = process(costs,edges)
    
        
    f = open("marathon.out", "w")

    if(answer=="None"): f.write(answer)
    else:
        f.write(str(len(answer))+"\n")
        for i in answer:
            f.write(i+" ")


if __name__== "__main__":
    main()