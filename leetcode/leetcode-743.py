class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a,b,c in times:
            graph[a].append((b,c))       
        queue=[(k,0)]
        total_fee={}
        total_fee[k]=0
        while queue:
            v = queue.pop(0)
            for w in graph[v[0]]:
                if w[0] not in total_fee:
                    fee=total_fee[v[0]]+w[1]
                    total_fee[w[0]]=fee
                    queue.append(w)
                else:
                    fee=total_fee[v[0]]+w[1]
                    if(total_fee[w[0]]>fee):
                        total_fee[w[0]]=fee
                        queue.append(w)
        print(total_fee)
        if(len(total_fee)==n): return max(total_fee.values())
        return -1