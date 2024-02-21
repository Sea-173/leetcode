"""
题目描述：
    给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

    回文串 是正着读和反着读都一样的字符串。
"""

"""
思路总结：
    由于分类在回溯，所以没有考虑用dp做，其实二维dp可以到达很高的速率。

    回溯的思想很简单：
        对s中的每个字符，进行分割和不分割两种情况，然后对不分割的情况进行递归，对分割的情况，如果当前字符串是回文串，则进行递归。
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        length = len(s)
        def isCircle(sub_s):
            """
            判断一个字符串是否是回文串

            参数：
                sub_s：待判断的字符串

            返回值：
                如果字符串是回文串，返回True；否则返回False
            """
            mid = len(sub_s) // 2
            for i in range(mid):
                if sub_s[i] != sub_s[-(i+1)]:
                    return False
            return True

        def partitionSubStr(cur_str, cur_pos, cur_result):
            # print('str, pos, result', cur_str, cur_pos, cur_result)
            new_cur_result = cur_result.copy()
            if cur_pos == length:
                if isCircle(cur_str):
                    new_cur_result.append(cur_str)
                    result.append(new_cur_result)
                return
            
            # 不分割
            partitionSubStr(cur_str+s[cur_pos], cur_pos+1, new_cur_result)

            # 分割
            if cur_str != "" and isCircle(cur_str):
                new_cur_result.append(cur_str)
                partitionSubStr(s[cur_pos], cur_pos+1, new_cur_result)
            return
        partitionSubStr("", 0, [])
        return result
            