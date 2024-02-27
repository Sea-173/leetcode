"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, index):
            if index == len(word):
                return True
            for x, y in ([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]):
                if x< 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                    continue

                if board[x][y] == word[index]:
                    print(x, y)
                    board[x][y] = '#'
                    if dfs(x, y, index + 1):
                        return True
                    board[x][y] = word[index]
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if dfs(i, j, 1):
                        return True
                    board[i][j] = word[0]
        return False
