"""
在二维平面上的 x 轴上，放置着一些方块。

给你一个二维整数数组 positions ，其中 positions[i] = [lefti, sideLengthi] 表示：第 i 个方块边长为 sideLengthi ，其左侧边与 x 轴上坐标点 lefti 对齐。

每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 另一个正方形的顶边 或者是 x 轴上 。一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。

在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。

返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度。
"""

"""
思路总结：
    主要是对过程的模仿，注意每种情况的分类讨论。
"""


from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # mark = [[left, right, height], ]
        result = [positions[0][1]]
        mark = [[positions[0][0], positions[0][0] + positions[0][1], positions[0][1]]]

        def update_mark(cur_p, mark):
            left, right = cur_p[0], cur_p[0] + cur_p[1]
            max_height = cur_p[1]
            for m in range(len(mark)):
                if (mark[m][0] < left and mark[m][1] > left) or (mark[m][0] < right and mark[m][1] > right) or (
                        left <= mark[m][0] and right >= mark[m][1]) or (left >= mark[m][0] and right <= mark[m][1]):
                    max_height = max(max_height, mark[m][2] + cur_p[1])
            if max_height == cur_p[1]:
                if mark[0][0] >= right:
                    mark.insert(0, [left, right, cur_p[1]])
                elif mark[-1][1] <= left:
                    mark.append([left, right, cur_p[1]])
                for m in range(1, len(mark)):
                    if mark[m - 1][1] < left and mark[m][0] > right:
                        mark.insert(m, [left, right, cur_p[1]])
                        break
            else:
                new_mark = []
                for m in range(len(mark)):
                    if mark[m][1] <= left:
                        new_mark.append(mark[m])
                        continue
                    if mark[m][0] >= right:
                        new_mark.append(mark[m])
                        continue
                    if mark[m][0] <= left and mark[m][1] >= right:
                        new_mark.append([mark[m][0], left, mark[m][2]])
                        new_mark.append([left, right, max_height])
                        new_mark.append([right, mark[m][1], mark[m][2]])
                    if mark[m][0] < left and mark[m][1] < right:
                        new_mark.append([mark[m][0], left, mark[m][2]])
                        if m == len(mark) - 1 or mark[m+1][0] >= right:
                            new_mark.append([left, right, max_height])
                    if mark[m][0] >= left and mark[m][1] <= right:
                        if m == len(mark) - 1 or mark[m+1][0] >= right:
                            new_mark.append([left, right, max_height])
                    if mark[m][0] > left and mark[m][1] > right:
                        new_mark.append([left, right, max_height])
                        new_mark.append([right, mark[m][1], mark[m][2]])
                mark = new_mark
            return max_height, mark

        for p in range(1, len(positions)):
            max_height, mark = update_mark(positions[p], mark)
            result.append(max(max_height, result[-1]))
        return result

s1 = Solution()
positions = [[3,2],[8,3],[1,4],[8,10],[9,3]]
result = s1.fallingSquares(positions)
print(result)