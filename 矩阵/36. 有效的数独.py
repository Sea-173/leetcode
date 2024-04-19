"""
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_rows = [[0 for _ in range(9)] for _ in range(9)]
        check_cols = [[0 for _ in range(9)] for _ in range(9)]
        check_sub = [[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    index = int(c) - 1
                    check_rows[i][index] += 1
                    check_cols[j][index] += 1
                    check_sub[i // 3][j // 3][index] += 1
                    if check_rows[i][index] > 1 or check_cols[j][index] > 1 or check_sub[i // 3][j // 3][index] > 1:
                        return False
        return True
