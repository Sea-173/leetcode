"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
"""

class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = 0
        num = 0
        len_s = len(s)

        i = 0
        while i < len_s:
            if s[i].isnumeric():
                # 遇到数字，将其与后续连续的数字拼接起来
                for j in range(i, len_s):
                    if s[j].isnumeric():
                        num = num * 10 + int(s[j])
                    else:
                        break
                for k in range(j, len_s):
                    if s[k] == '[':
                        stack += 1
                    elif s[k] == ']':
                        stack -= 1
                        if stack == 0:
                            sub_s = self.decodeString(s[j+1:k])
                            result += sub_s * num
                            num = 0
                            break
                i = k + 1
            elif s[i].isalpha():
                result += s[i]
                i += 1
        return result

# s1 = Solution()ß
# s = "3[a]2[bc]"
# print(s1.decodeString(s))
                               