"""
给你两个字符串 s 和 t，每个字符串中的字符都不重复，且 t 是 s 的一个排列。

排列差 定义为 s 和 t 中每个字符在两个字符串中位置的绝对差值之和。

返回 s 和 t 之间的 排列差 。
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        c_map = {}
        for index, (i, j) in enumerate(zip(s, t)):
            if i not in c_map:
                c_map[i] = index
            else:
                result += abs(index - c_map[i])

            if j not in c_map:
                c_map[j] = index
            else:
                result += abs(index - c_map[j])
        return result