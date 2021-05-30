class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        seen=set()
        finished=set()
        flag=[]
        
        def dfs(current):
            if(flag): return
            
            if(current in seen):
                flag.append(1)
                return
            if(current in finished): return
            seen.add(current)
            for i in graph[current]:
                dfs(i)
            seen.remove(current)
            finished.add(current)
            
            
        for i in list(graph):
            
                dfs(i)
        if(flag): return False
        return True   
      
        