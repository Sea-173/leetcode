"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
"""

"""
思路总结：
    经典贪心算法，下面的解法有点笨，保存了整个数组。
    好的解法应该是只保存当前所能到达的最远位置，然后每次更新这个位置，如果更新后的位置大于等于数组长度，则返回True。
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        stack = [0 for _ in nums]
        stack[0] = nums[0]
        cur = 0

        while cur < len(stack):
            if stack[-1] == 1:
                return True
            if stack[cur] == 0:
                cur += 1
                continue

            tmp = cur
            for _ in range(1, nums[cur]+1):
                if tmp >= len(stack):
                    return True
                tmp += 1
                stack[tmp] = 1
            cur += 1
        return False

# 20240410
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_max, cur = 0, 0
        n = len(nums)
        while cur < n:
            old_max = cur_max
            for p in range(cur, old_max+1):
                if p >= n-1:
                    return True
                cur_max = max(cur_max, p + nums[p])
            if cur_max == old_max:
                break
            cur = old_max
        return cur_max >= n
        
s1 = Solution()
nums = [2,3,1,1,4]
print(s1.canJump(nums))