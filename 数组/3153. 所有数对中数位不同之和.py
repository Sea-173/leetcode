"""
你有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。

两个整数的 数位不同 指的是两个整数 相同 位置上不同数字的数目。

请你返回 nums 中 所有 整数对里，数位不同之和。
"""


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        count = []

        n0 = nums[0]
        while n0 > 0:
            cur = n0 % 10
            n0 = n0 // 10
            count.append([0 for _ in range(10)])
            count[-1][cur] += 1

        for n in range(1, len(nums)):
            pos = 0
            while nums[n] > 0:
                cur = nums[n] % 10
                nums[n] = nums[n] // 10
                count[pos][cur] += 1
                pos += 1

        result = 0
        for c in count:
            for i in range(9):
                if c[i] == 0:
                    continue

                result += c[i] * sum(c[i + 1:])

        return result

