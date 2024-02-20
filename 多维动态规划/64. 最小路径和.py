"""
题目描述：
    给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

    说明：每次只能向下或者向右移动一步。
"""

"""
思路总结：
    多维dp和一维dp相似，主要区别就是dp数组的维度。
    这道题是典型的2维dp，递推关系仅仅只来自于上面的元素或者左边的元素，非常好写。
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        # 初始化第一行
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        # 初始化第一列
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                minn = min(dp[i-1][j], dp[i][j-1])
                dp[i][j] = grid[i][j] + minn
        print(dp)
        return dp[m-1][n-1]
