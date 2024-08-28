class Solution(object):
    def countSubIslands(self, grid1, grid2):
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            if grid1[i][j] == 0:  
                return False
            grid2[i][j] = 0  
            result = True
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                result = dfs(i + di, j + dj) and result
            return result

        m, n = len(grid1), len(grid2[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:  
                    if dfs(i, j): 
                        count += 1
        return count
