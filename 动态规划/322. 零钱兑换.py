"""
思路总结：
    零钱兑换是经典的动态规划问题，与完全平方数那道题类似。
    - 动态规划问题，首先列出动态规划数组dp，为了方便，通常长度为n+1。
    - 查看是否需要对dp[1]和dp[2]赋初始值。
    - 开始循环，每次进入循环都需要获得一个dp[i]。
        - 零钱兑换问题和完全平方数问题，特殊在递推关系是由i之前的哪个值获得不确定，所以在循环中还有一次循环，比较找到i之前递推关系的最优解。
    - 返回dp[n]即可
"""

import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        dp = [-1 for _ in range(amount + 1)]

        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            minn = sys.maxsize
            for c in coins:
                if i - c < 0:
                    continue
                if dp[i-c] != -1:
                    minn = min(minn, dp[i-c] + 1)
            if minn != sys.maxsize:
                dp[i] = minn
            else:
                dp[i] = -1
        return dp[amount]