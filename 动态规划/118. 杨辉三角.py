"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1 for _ in range(i+1)]
            for j in range(1, i):
                tmp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(tmp)
        return res