"""
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。
"""

"""
思路总结
    123456X7Y8 - 12345687
    XY87654321 - 12345678
    412356X7Y8 - 41235687
    4X3876Y521 - 45123678
    4235X7Y861 - 42358167

    总的来说就是首先找到X的位置：
        从右往左第一个非单调递增的位置
    然后从X位置开始往右找到第一个大于nums[X]的位置Y，
    交换X和Y，然后翻转从X+1到最后的数组
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, begin, end):
            while begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
                end -= 1
            return

        len_n = len(nums)
        x_place = len_n - 1
        n = len_n - 1
        while n >= 0:
            x_place -= 1
            if nums[n-1] < nums[n]:
                break
            n -= 1
            
        print(x_place)
        if x_place == -1:
            reverse(nums, 0, len_n-1)
            return nums
        
        y_place = x_place + 1
        for n in range(x_place+1, len_n):
            if nums[x_place] < nums[n]:
                y_place = n
            else:
                break
        print(x_place, y_place)
        nums[x_place], nums[y_place] = nums[y_place], nums[x_place]
        
        reverse(nums, x_place+1, len_n-1)
        return nums

s = Solution()
nums = [2,3,1]
result = s.nextPermutation(nums)
print(result)