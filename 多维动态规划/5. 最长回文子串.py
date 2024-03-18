"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
"""

"""
例子：
    'babab'
    1 0 1 0 1
    0 1 0 1 0
    0 0 1 0 1
    0 0 0 1 0
    0 0 0 0 1

思路总结
    这道题按题意应该是多维动态规划，但是由于回文字符串需要从中间向两边检查，所以会存在大量冗余的循环
    换成广搜的模式，把每个子回文串push进栈中，再挨个出栈检查，每次只检查当前出栈子串s，和s前后一个字符是否是回文串，这样就大大减少了冗余检查。
    有一个点要注意，就是在初始化栈的时候，需要考虑特殊的回文子串，即'bb'型，这种需要特判，但是好在初始化一共也只需要一次循环即可。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth = len(s)
        if lenth < 2:
            return s
        stack = []
        i = 0
        while i < lenth:
            stack.append([i,i])
            if i > 0 and s[i] == s[i-1]:
                for j in range(i, lenth):
                    if s[i-1] == s[j]:
                        stack.append([i-1, j])
                    else:
                        stack.append([j, j])
                        break
                i = j
            i += 1
            
        max_begin, max_len = 0, 0
        while stack:
            cur_center = stack.pop(0)
            if cur_center[1] - cur_center[0] > max_len:
                max_begin = cur_center[0]
                max_len = cur_center[1] - cur_center[0]
            if cur_center[0] == 0 or cur_center[0] == lenth - 1 or cur_center[1] == 0 or cur_center[1] == lenth - 1:
                continue
            if s[cur_center[0]-1] == s[cur_center[1]+1]:
                stack.append([cur_center[0]-1, cur_center[1]+1])
        return s[max_begin:max_begin+max_len+1]
        
