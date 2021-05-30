class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph=collections.defaultdict(list)
        for a,b,c in flights:
            graph[a].append((b,c))
        queue=[(0,src,0)]
        print(graph)
        while queue:
            time ,node , between = heapq.heappop(queue)
            if (node==dst): return time
            if(between<=K): 
                    for v,w in graph[node]:
                        alt = time+w
                        heapq.heappush(queue,(alt,v,between+1))   
                        
        return -1