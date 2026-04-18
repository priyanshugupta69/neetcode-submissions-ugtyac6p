class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = set()

        def dfs(i: int, j: int , seen: set((int,int))) -> int:
            if i >= m or j >= n or i < 0 or j < 0:
                return 0
            
            if (i,j) in seen:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            seen.add((i,j))
            
            return 1 + dfs(i + 1, j, seen) +  dfs(i-1, j , seen) + dfs(i, j + 1, seen) + dfs(i, j -1, seen)
            
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(dfs(i,j,vis), ans)
        
        return ans