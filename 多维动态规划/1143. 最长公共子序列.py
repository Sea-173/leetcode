"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
"""

"""
  a b c d e
a 1 1 1 1 1
c 1 1 2 2 2
e 1 1 2 2 3

  a b c d e
c 0 0 1 1 1
e 0 0 1 1 2
a 1 1 1 1 2

  j m j k b b k v
b 0 0 0 0 1 1 1 1
s 0 0 0 0 1 1 1 1
b 0 0 0 0 1 2
i
n
i
n
m
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0 for _ in range(len2)] for _ in range(len1)]

        if text1[0] == text2[0]:
            dp[0][0] = 1

        # 初始化第一行
        for i in range(1, len2):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i-1]
        # 初始化第一列
        for j in range(1, len1):
            if text2[0] == text1[j]:
                dp[j][0] = 1
            else:
                dp[j][0] = dp[j-1][0]

        for i in range(1, len1):
            for j in range(1, len2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]