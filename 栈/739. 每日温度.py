"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
"""

"""
思路总结：
    要使用一个栈来维持没有找到更大值的index，
    所以在遍历元素时，首先判断是否有元素需要出栈
    如果当前元素大于栈顶元素，则出栈，并记录当前元素距离栈顶元素的index
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in temperatures]
        for index, t in enumerate(temperatures):
            if len(stack) == 0 or t <= temperatures[stack[-1]]:
                stack.append(index)
            else:
                while len(stack) > 0 and t > temperatures[stack[-1]]:
                    cur = stack.pop()
                    result[cur] = index - cur
                stack.append(index)
        return result
    
s = Solution()
t = [73,74,75,71,69,72,76,73]
print(s.dailyTemperatures(t))