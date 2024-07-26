"""
给你一个 正 整数数组 nums 。

将 nums 分成两个数组：nums1 和 nums2 ，并满足下述条件：

数组 nums 中的每个元素都属于数组 nums1 或数组 nums2 。
两个数组都 非空 。
分区值 最小 。
分区值的计算方法是 |max(nums1) - min(nums2)| 。

其中，max(nums1) 表示数组 nums1 中的最大元素，min(nums2) 表示数组 nums2 中的最小元素。

返回表示分区值的整数。
"""

"""
思路总结：
    该题的问题只是转换题目说法，理解到是求数组中绝对值相差最小的两个数即可
"""

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums = nums.sort()
        min_divide = 1e5
        for n in range(1, len(nums)):
            min_divide = min(min_divide, abs(nums[n] - nums[n-1]))
        return min_divide
