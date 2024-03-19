"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""

"""
1 5 5 11
1 6 11 22
22 21 16 11

0 1
1 2
2 3

1 1 1 1 1
1 2 3 4 5
5 4 3 2 1
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n_num = len(nums)
        if n_num < 2:
            return False
        
        # 求得最大项，目标项，总和
        max_item = 0
        target_num = 0
        all_sum = 0
        for n in nums:
            max_item = max(max_item, n)
            all_sum += n
        
        # 如果总和为奇数，不可分
        if all_sum % 2 != 0:
            return False
        target_num = all_sum // 2
        # 如果最大项大于目标项，不可分
        if max_item > target_num:
            return False
        
        # dp数组
        # dp[i][j] 代表 从nums[0]到nums[i]的数中，是否可以抽取几个数的和为j
        dp = [[False for _ in range(target_num+1)] for _ in range(n_num)]

        # dp[i][0] = True
        for i in range(n_num):
            dp[i][0] = True

        # dp[0][nums[0]] = True
        dp[0][nums[0]] = True
        
        for i in range(1, n_num):
            for j in range(1, target_num+1):
                # 如果nums[i] > j,则说明不能选取nums[i]，因此dp[i][j]和dp[i-1][j]选择范围一致，结果一致
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                # 否则分两种情况
                #   不选择nums[i]，即nums[0]～nums[i-1]能否凑和得到j
                #   选择nums[i]，即nums[0]~nums[i-1]能否凑和得到j-nums[i]
                else:
                    if dp[i-1][j] or dp[i-1][j-nums[i]]:
                        dp[i][j] = True
        return dp[-1][-1]
            


