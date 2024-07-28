"""
给你一个字符串 s 和一个整数 k 。

定义函数 distance(s1, s2) ，用于衡量两个长度为 n 的字符串 s1 和 s2 之间的距离，即：

字符 'a' 到 'z' 按 循环 顺序排列，对于区间 [0, n - 1] 中的 i ，计算所有「 s1[i] 和 s2[i] 之间 最小距离」的 和 。
例如，distance("ab", "cd") == 4 ，且 distance("a", "z") == 1 。

你可以对字符串 s 执行 任意次 操作。在每次操作中，可以将 s 中的一个字母 改变 为 任意 其他小写英文字母。

返回一个字符串，表示在执行一些操作后你可以得到的 字典序最小 的字符串 t ，且满足 distance(s, t) <= k 。
"""


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def find_small_one(cur_c, cur_k):
            minus = abs(ord('a') - ord(cur_c))
            plus = 26 - minus
            real_k = min(minus, plus)
            if real_k <= cur_k:
                return 'a', cur_k - real_k
            else:
                return chr(ord(cur_c) - cur_k), 0

        result = ''
        for si in s:
            if k != 0:
                cur_c, k = find_small_one(si, k)
                result += cur_c
            else:
                result += si
        return result

