"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalpha():
                if i.isupper():
                    ans += i.lower()
                else:
                    ans += i
            if i.isnumeric():
                ans += i
        n = len(ans)
        if n < 2:
            return True
        if n % 2 == 0:
            return ans[:n//2] == ans[n//2:][::-1]
        else:
            return ans[:n//2] == ans[n//2+1:][::-1]

