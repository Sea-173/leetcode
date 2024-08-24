"""
给你两个整数 n 和 x 。你需要构造一个长度为 n 的 正整数 数组 nums ，对于所有 0 <= i < n - 1 ，满足 nums[i + 1] 大于 nums[i] ，并且数组 nums 中所有元素的按位 AND 运算结果为 x 。

返回 nums[n - 1] 可能的 最小 值。
"""

"""
0001 1  0001010
0011 3
0101 5
0111 7
1001
1001
    101
0000000
0000101
0100111

"""

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bin_x = bin(x)[2:]
        bin_n = bin(n-1)[2:]
        result = [0 for _ in range(len(bin_x) + len(bin_n))]

        for bx in range(len(bin_x)):
            result[len(bin_n)+bx] = int(bin_x[bx])

        bn = len(bin_n)-1
        for re in range(len(result)-1, -1, -1):
            if bn < 0:
                break
            if result[re] == 0:
                result[re] = int(bin_n[bn])
                bn -= 1

        decimal_value = 0
        for i, bit in enumerate(reversed(result)):
            decimal_value += bit * (2 ** i)
        return decimal_value

s = Solution()
result = s.minEnd(4, 1)
print(result)