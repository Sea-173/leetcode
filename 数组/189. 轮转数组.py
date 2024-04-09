"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k := (k % len(nums)):
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
