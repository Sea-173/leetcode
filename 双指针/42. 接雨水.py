"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left, leftMax = 0, 0
        right, rightMax = len(height) - 1, 0
        res = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                res += leftMax - height[left]
                left += 1
            else:
                res += rightMax - height[right]
                right -= 1
        return res