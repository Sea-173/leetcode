"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""

class Solution:
    # 快排改进
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(nums, left, right):
            pivot = random.randint(left, right)
            nums[pivot], nums[left] = nums[left], nums[pivot]
            tar = nums[left]

            L, R = left, right
            while L < R:
                while L < R and nums[R] >= tar:
                    R -= 1
                nums[L] = nums[R]
                while L < R and nums[L] <= tar:
                    L += 1
                nums[R] = nums[L]

            nums[L] = tar
            if L == len(nums) - k:
                return nums[L]
            elif L < len(nums) - k:
                while L < len(nums) - k and nums[L] == nums[L+1]:
                    L += 1
                if L == len(nums) - k:
                    return nums[L]
                return quickSort(nums, L + 1, right)
            else:
                while L > len(nums) - k and nums[L-1] == nums[L]:
                    L -= 1
                if L == len(nums) - k:
                    return nums[L]
                return quickSort(nums, left, L - 1)
        return quickSort(nums, 0, len(nums) - 1)
            
                