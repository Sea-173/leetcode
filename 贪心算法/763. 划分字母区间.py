"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。
"""

"""
思路总结：
    贪心算法，每遇到一个新的字符就分割，遇到重复的字符就遍历之前的分割结果并调整。
    具体针对这道题，
        就是使用pos字典来存储遇到的字符的起始位置（就是第一个这个字符所在的位置），
        遇到重复字符时，需要重新分割，分割区间就是起始位置到当前位置。
"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        part = []
        cur = 0

        def adjustPos(pos, part, s, cur):
            char = s[cur]
            if char not in pos:
                pos[char] = cur
                part.append(cur)
                return part
            else:
                begin_pos = pos[char]
                end_pos = cur
                new_part = []
                for i in range(len(part)):
                    if part[i] < begin_pos:
                        new_part.append(part[i])
                        continue
                    break
                new_part.append(cur)
            return new_part
                    

        while cur < len(s):
            part = adjustPos(pos, part, s, cur)
            cur += 1
        length = []
        old = -1
        for i in part:
            length.append(i - old)
            old = i
        return length

s1 = Solution()
# s = "ababcbacadefegdehijhklij"
s = "eccbbbbdec"
print(s1.partitionLabels(s))
