"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""

"""
思路总结：
    栈的特点是先进后出，
    所以每次遇到一个左括号，就入栈；
    遇到一个右括号，就出栈并判断是否匹配；
    如果最后栈为空，说明括号匹配
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if cur == '(' and i != ')' or cur == '{' and i != '}' or cur == '[' and i != ']':
                    return False
        return not stack