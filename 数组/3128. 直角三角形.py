"""
给你一个二维 boolean 矩阵 grid 。

请你返回使用 grid 中的 3 个元素可以构建的 直角三角形 数目，且满足 3 个元素值 都 为 1 。

注意：

如果 grid 中 3 个元素满足：一个元素与另一个元素在 同一行，同时与第三个元素在 同一列 ，
那么这 3 个元素称为一个 直角三角形 。这 3 个元素互相之间不需要相邻。
"""

"""
思路总结：
    主要是要观察到，这道题问的是一个行和乘列和的问题
"""



class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        result = 0
        row_sums = [sum(grid[x]) for x in range(len(grid[0]))]
        col_sums = [sum(col) for col in zip(*grid)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    col_sum = col_sums[j] -1
                    row_sum = row_sums[i] - 1
                    result += row_sum * col_sum
        return result