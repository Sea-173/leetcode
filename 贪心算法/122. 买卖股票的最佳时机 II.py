"""
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min_price = prices[0]
        cur_max_profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            # print(prices[i], max_profit, cur_max_profit, cur_min_price)
            if prices[i] < prices[i-1]:
                max_profit += cur_max_profit
                cur_min_price = prices[i]
                cur_max_profit = 0

            # if prices[i] < cur_min_price:
            #     max_profit += cur_max_profit
            #     cur_max_profit = 0
            #     cur_min_price = prices[i]
            else:
                cur_max_profit = max(cur_max_profit, prices[i] - cur_min_price)
        max_profit += cur_max_profit
        # print(max_profit)
        return max_profit

s = Solution()
prices = [7,6,4,3,1]
s.maxProfit(prices)