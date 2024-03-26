"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
"""

"""
思路总结：
    一定要多一行，代表从""到word的编辑次数
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        if len1 * len2 == 0:
            return max(len1, len2)
        dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
        for i in range(len2+1):
            dp[i][0] = i
        for j in range(len1+1):
            dp[0][j] = j
        
        for i in range(1, len2+1):
            for j in range(1, len1+1):
                dp[i][j] = dp[i-1][j-1] if word1[j-1] == word2[i-1] else min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
    
    def minDistance2(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        # 有一个字符串为空串
        if n * m == 0:
            return n + m
        
        # DP 数组
        D = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j
        
        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)
        
        return D[-1][-1]
    

s1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
s2 = "ultramicroscopically"

s = Solution()

result1 = s.minDistance(s1, s2)
result2 = s.minDistance2(s2, s1)

for i in range(20):
    print(result1[i], result2[i+1][1:])