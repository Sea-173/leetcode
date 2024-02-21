"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""

"""
思路总结：
    easy回溯
    三个有问题的条件：
        上面
        左斜
        右斜
    判断一下直接递归就行
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = 0
        def backtrack(row, cur_queens):
            if row == n:
                result+= 1
                return
            
            for col in range(n):
                tf = True
                # 上面
                for i in range(row):
                    if cur_queens[i][col] ==  'Q':
                        tf = False
                        break
                if not tf:
                    continue
                # 左斜上方
                for i in range(min(col, row)):
                    if cur_queens[row-i][col-i] == 'Q':
                        tf = False
                        break
                if not tf:
                    continue
                # 右斜上方
                for i in range(min(n-col, row)):
                    if cur_queens[row-i][col+i] == 'Q':
                        tf = False
                if not tf:
                    continue

                new_cq = cur_queens.copy()
                new_cq[row][col] = 'Q'
                backtrack(row+1, new_cq)
            return
        backtrack(0, [['.' for _ in range(n)] for _ in range(n)])
        return result
            