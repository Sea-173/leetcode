"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""

"""
思路总结：
    主要是需要判断二分点处于旋转点的左边还是右边，然后分别进行处理。
    次要是注意边界：
        左闭右闭
        mid有可能等于left，所以在这种情况下需要递归右边区间
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, left, right, target):
            if left > right:
                return -1
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[left]:
                # 左边有序
                if target <= nums[mid] and target >= nums[left]:
                    return binary_search(nums, left, mid-1, target)
                else:
                    return binary_search(nums, mid+1, right, target)
            else:
                # 右边有序
                if target >= nums[mid] and target <= nums[right]:
                    return binary_search(nums, mid+1, right, target)
                else:
                    return binary_search(nums, left, mid-1, target)
        return binary_search(nums, 0, len(nums)-1, target)
