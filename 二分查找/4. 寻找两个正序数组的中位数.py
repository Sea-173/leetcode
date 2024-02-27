"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        n1, n2 = 0, 0
        for i in range(m+n//2):
            if nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
        if (m + n) % 2 == 0:
            return min(nums1[n1], nums2[n2])
        else:
            return (nums1[n1] + nums2[n])/2