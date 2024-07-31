"""
给你一个下标从 0 开始的二维数组 variables ，其中 variables[i] = [ai, bi, ci, mi]，以及一个整数 target 。

如果满足以下公式，则下标 i 是 好下标：

0 <= i < variables.length
((aibi % 10)ci) % mi == target
返回一个由 好下标 组成的数组，顺序不限 。
"""

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        result = []
        for i in range(len(variables)):
            current = (((variables[i][0] ** variables[i][1]) % 10) ** variables[i][2]) % variables[i][3]
            if current == target:
                result.append(i)
        return result
