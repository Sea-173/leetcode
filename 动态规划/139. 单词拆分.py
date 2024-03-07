"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

"""

"""
思路总结
    经典动态规划，设当前位置为cur，dp[i]表示s[:i+1]可以由wordDict表示，则有两种情况
        - s[:cur+1]在在字典中，直接记录
        - 遍历0-cur，如果dp[i]为True，就检查s[i+1:cur+1]是否字典中
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        
        for cur in range(len(s)):
            if s[:cur+1] in wordDict:
                dp[cur] = True
                continue
            for i in range(cur, -1, -1):
                if dp[i] and s[i+1:cur+1] in wordDict:
                    dp[cur] = True
                    break
        return dp[-1]