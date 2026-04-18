from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        seen = set()

        m = len(grid)
        n = len(grid[0])

        def addEl(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or (i,j) in seen or grid[i][j] == 0:
                return
            
            dq.append((i,j))
            seen.add((i,j))

        freshCount = 0

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i,j))
                    seen.add((i,j))
                elif grid[i][j] == 1:
                    freshCount += 1

        if len(dq) == 0 and freshCount == 0:
            return 0
        
        dist = 0
        
        while dq:
            for _ in range(len(dq)):
                (i,j) = dq.popleft()
                grid[i][j] = 2
                addEl(i+1, j)
                addEl(i-1,j)
                addEl(i,j+1)
                addEl(i,j-1)
            dist += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return dist - 1
            

        