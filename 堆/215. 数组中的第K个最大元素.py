"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""

class Solution:
    # 快排改进
    def findKthLargest(self, nums: List[int], k: int) -> int:
        L, R = 0, len(nums)

        def quickSort(L, R):
            if L >= R:
                return
            
            if R - L == 1:
                if nums[L] > nums[R]:
                    temp = nums[R]
                    nums[R] = nums[L]
                    nums[L] = temp
            
            mid_val = nums[L]
            old_L, old_R = L, R

            while L < R:
                tf = 0
                while L < R:
                    if nums[L] > mid_val:
                        tf += 1
                        break
                    L += 1
                while L < R:
                    if nums[R] < mid_val:
                        tf += 1
                        break
                    R -= 1
                if tf == 2:
                    temp = nums[L]
                    nums[L] = nums[R]
                    nums[R] = temp
            
                