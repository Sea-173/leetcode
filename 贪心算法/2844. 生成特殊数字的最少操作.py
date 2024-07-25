"""
给你一个下标从 0 开始的字符串 num ，表示一个非负整数。

在一次操作中，您可以选择 num 的任意一位数字并将其删除。请注意，如果你删除 num 中的所有数字，则 num 变为 0。

返回最少需要多少次操作可以使 num 变成特殊数字。

如果整数 x 能被 25 整除，则该整数 x 被认为是特殊数字。
"""

"""
思路总结：
    贪心算法，从右至左遍历数组，如果遇见25, 50, 00就返回
    注意特判
"""

class Solution:
    def minimumOperations(self, num: str) -> int:
        len_n = len(num)
        if len_n == 1:
            if num[0] == '0':
                return 0
            else:
                return 1
        del_num = 0
        is_five = False # 2, 7
        is_zero = False # 5, 0
        for i in range(len_n-1, -1, -1):
            if (num[i] == '2' or num[i] == '7') and is_five:
                if is_five and is_zero:
                    del_num += 1
                return del_num
            if (num[i] == '5' or num[i] == '0') and is_zero:
                if is_five and is_zero:
                    del_num += 1
                return del_num
            if num[i] == '5':
                if is_five:
                    del_num += 1
                else:
                    is_five = True
                continue
            if num[i] == '0':
                if is_zero:
                    del_num += 1
                else:
                    is_zero = True
                continue
            del_num += 1

        return len_n - is_zero



