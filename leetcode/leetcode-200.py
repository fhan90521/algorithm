class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counts=0
        def dfs(i,k):
            grid[i][k]=0
            if( i+1<len(grid) and grid[i+1][k]=='1'):
                dfs(i+1,k)
            if( k+1<len(grid[i]) and grid[i][k+1]=='1'):
                dfs(i,k+1)
            if( i-1>=0 and grid[i-1][k]=='1'):
                dfs(i-1,k)
            if( k-1>=0 and grid[i][k-1]=='1'):
                dfs(i,k-1)
            return
        for i in range(len(grid)):
            for k in range(len(grid[i])):
                if( grid[i][k]=='1'):
                    
                    counts+=1
                    seen=dfs(i,k)
        
        return counts