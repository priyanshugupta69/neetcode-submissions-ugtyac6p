class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.seen = set()

        m = len(grid)
        n = len(grid[0])

        sum = 0

        def dfs(grid,row, col) -> int:
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            
            if grid[row][col] == "0":
                return 0
            
            if (row,col) in self.seen:
                return 0
            
            self.seen.add((row,col))
            
            dfs(grid, row + 1, col) + dfs(grid, row - 1, col) + dfs(grid, row, col + 1) + dfs(grid, row, col-1)

            return 1
        
        for i in range(m):
            for j in range(n):
                sum += dfs(grid, i , j)
        
        return sum


            
            
                    

            


        