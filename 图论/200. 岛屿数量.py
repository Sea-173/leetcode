"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

"""

"""
思路总结：
    扫雷思想，1表示岛，0表示水，-1表示已经扫描过的岛
    遍历数组，在遇到一个岛时递归找到所有相邻的1， 并标记为-1， 一次遍历即可找到所有岛
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markIsland(i, j):
            if i > 0 and grid[i-1][j] == '1':
                grid[i-1][j] = '-1'
                markIsland(i-1, j)
            
            if i < len(grid)-1 and grid[i+1][j] == '1':
                grid[i+1][j] = '-1'
                markIsland(i+1, j)

            if j > 0 and grid[i][j-1] == '1':
                grid[i][j-1] = '-1'
                markIsland(i, j-1)

            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                grid[i][j+1] = '-1'
                markIsland(i, j+1)
            return
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    markIsland(i, j)
                    num_islands += 1
        return num_islands
