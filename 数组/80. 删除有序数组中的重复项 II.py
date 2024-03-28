"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""

"""
思路总结
    使用lenth指针来代替额外数组空间
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lenth = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[lenth]:
                lenth += 1
                nums[lenth] = nums[i]
                count = 1
            else:
                count += 1
                if count > 2:
                    continue
                else:
                    lenth += 1
                    nums[lenth] = nums[i]
        return lenth + 1

