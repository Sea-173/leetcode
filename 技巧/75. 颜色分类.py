"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。
"""

"""
思路总结
    双指针，left指向从前向后第一个不是0的位置，right指向从后向前第一个不是2点位置，
        遇到0就丢到left位置，
        遇到1就不变，
        遇到2就丢到right位置，注意这里需要再次检测换回来的数
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        size = len(nums)
        if size < 2:
            return
        
        left = 0
        right = size
        i = 0

        while i < right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 1:
                i += 1
            else:
                right -= 1
                nums[i], nums[right] = nums[right], nums[i]
        return
            
