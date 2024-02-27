"""
思路总结：
    快速排序的重点在于：
        1. 随机取pivot，达到平均时间复杂度
        2. 划分左右子序列，递归区间是(left, L-1) 和 (L+1, right))
        3. 循环中需要有个trick，就是从right向左递归，利用当前指针的位置存储信息，主要看代码中的循环
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, left, right):
            if left >= right:
                return

            pivot_idx = random.randint(left, right)
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]

            pivot = nums[left]
            L, R = left, right
            while L < R:
                while L < R and nums[R] >= pivot:
                    R -= 1
                nums[L] = nums[R]
                while L < R and nums[L] <= pivot:
                    L += 1
                nums[R] = nums[L]
            nums[L] = pivot

            rt = L
            if rt > left + 1:
                while rt > left + 1 and nums[rt] == nums[rt-1]:
                    rt -= 1
                quickSort(nums, left, L-1)
            rt = L
            if rt < right - 1:
                while rt < right - 1 and nums[rt] == nums[rt+1]:
                    rt += 1
                quickSort(nums, L+1, right)

        quickSort(nums, 0, len(nums) - 1)
        return nums
        