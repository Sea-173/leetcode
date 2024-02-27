"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
"""

"""
思路总结：
    
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        minutes = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = -1
                    queue.append([i, j])
        
        if queue == []:
            for i in grid:
                for j in i:
                    if j == 1:
                        return -1
            return 0
        
        while queue:
            minutes += 1
            # print(grid, queue)
            for q in range(len(queue)):
                i, j = queue.pop(0)
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if i + x < 0 or i + x >= m or j + y < 0 or j + y >= n:
                        continue
                    if grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = -1
                        queue.append([i+x, j+y])
        for i in grid:
            for j in i:
                if j == 1:
                    return -1

        return minutes
        
                                       