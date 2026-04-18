
from collections import deque
class Solution: 
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 - 1  # 2147483647
        dq = deque()
        m = len(grid)
        n = len(grid[0])
        visit = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dq.append((i,j))
                    visit.add((i,j))
        
        def addElement(i,j):
            if i < 0 or j < 0 or i >=m or j >=n or (i,j) in visit or grid[i][j] == -1:
                return
            
            dq.append((i,j))
            visit.add((i,j))
        
        dist = 0
        while dq:
            for i in range(len(dq)):
                (i,j) = dq.popleft()
                grid[i][j] = dist
                addElement(i+1,j)
                addElement(i-1, j)
                addElement(i, j -1)
                addElement(i, j + 1)
            dist += 1

            


        

        