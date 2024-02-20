"""
题目描述：
    给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

    你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

    返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""

"""
思路总结：
    这道题真是贪心算法么。。。
    首先有一个思路，就是在prices[i]进来的时候，有两种情况，
        一种是成为当前最小值，代替之前的最小值
        一种是成为最大值，代替之前的最大值，并且获取新的最大利润
    因为有时间顺序，所以不会出现其他情况，这样写一个循环就足够了
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = int(1e9)

        for p in prices:
            minPrice = min(minPrice, p)
            result = max(p-minPrice, result)
        
        return result