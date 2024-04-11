"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        ans = 1
        cur_max = nums[0]
        cur_min = 0
        while cur_max < n - 1:
            ans += 1
            old_max = cur_max
            for i in range(cur_min, cur_max + 1):
                if i + nums[i] > cur_max:
                    cur_max = i + nums[i]
            cur_min = old_max
        return ans

# 20240411
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        count = 1
        cur_begin = 0
        cur_end = nums[0]

        while cur_end < len(nums) - 1:
            cur_max = 0
            for i in range(cur_begin+1, cur_end+1):
                cur_max = max(cur_max, i + nums[i])
            cur_begin = cur_end
            cur_end = cur_max
            count += 1
        return count