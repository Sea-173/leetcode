"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 连续
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        min_len = len(nums)+1
        cur_sum = 0

        while R < len(nums):
            cur_sum += nums[R]
            while cur_sum >= target:
                min_len = min(min_len, R - L + 1)
                cur_sum -= nums[L]
                L += 1
            R += 1

        return min_len % (len(nums)+1)