"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续
子数组
（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。
"""

"""
思路总结
    这道动态规划有点不一样，在于需要同时记录之前的最小值和最大值
    考虑当前数nums[i]，可能为正数，则只需要考虑前一个位置的dp值，
    但是如果nums[i]为负数，那么需要考虑前一个位置有没有可能存在一个负的最小值，现在能够成为最大值。
    因此需要记录两组dp
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_dp, max_dp, ans_dp = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            minDP = min_dp
            maxDP = max_dp
            max_dp = max(maxDP * nums[i], max(minDP * nums[i], nums[i]))
            min_dp = min(minDP * nums[i], min(maxDP * nums[i], nums[i]))
            ans_dp = max(max_dp, ans_dp)
        return  ans_dp