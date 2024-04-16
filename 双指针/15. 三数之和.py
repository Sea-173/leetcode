"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        L = 0
        result = []

        while L <= len(nums) - 3:
            M, R = L + 1, len(nums) - 1

            while M < R:
                cur = nums[L] + nums[R] + nums[M]
                if cur == 0:
                    result.append([nums[L], nums[M], nums[R]])
                    while M < R and nums[M + 1] == nums[M]:
                        M += 1
                    M += 1
                    while M < R and nums[R - 1] == nums[R]:
                        R -= 1
                    R -= 1
                if cur < 0:
                    while M < R and nums[M + 1] == nums[M]:
                        M += 1
                    M += 1
                if cur > 0:
                    while M < R and nums[R - 1] == nums[R]:
                        R -= 1
                    R -= 1
            while L < R and nums[L] == nums[L + 1]:
                L += 1
            L += 1
        return result