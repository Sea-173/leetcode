"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
"""

"""
思路总结：
    利用字典存储已经出现的字母，没遇到一个字母时:
        若未出现过，新增字典，长度加1
        若出现过，删除字典中的开始到重复的部分，更新长度，更新开始位置。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        max_len, cur_len = 0, 0
        begin = 0
        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]] = i
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = i - temp[s[i]]
                new_begin = temp[s[i]] + 1
                for j in range(begin, temp[s[i]] + 1):
                    del temp[s[j]]
                begin = new_begin
                temp[s[i]] = i

        return max_len
