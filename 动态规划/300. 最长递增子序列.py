"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列。
"""

"""
思路总结
    动态规划，dp[i]表示以nums[i]为结尾的最长递增子序列
    遍历nums，并记录在nums[i]之前的最长递增子序列长度，
        挨个比较nums[0~i-1]，如果nums[j]<nums[i]，则代表i位置可能的最长子序列是dp[j]+1
    返回dp中最大值即可
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]

        for n in range(len(nums)):
            for i in range(n):
                if nums[i] < nums[n]:
                    dp[n] = max(dp[n], dp[i]+1)
        return max(dp)
            