"""
给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。

炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。xi 和 yi 表示第 i 个炸弹的 X 和 Y 坐标，ri 表示爆炸范围的 半径 。

你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。

给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。
"""


class Solution:

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        max_count = 1

        def search_one(bombs, cur) -> []:
            root = [cur]
            result = [cur]

            while root != []:
                p = root.pop()
                for i in range(len(bombs)):
                    if i in result:
                        continue
                    if (bombs[i][0] - bombs[p][0]) ** 2 + (bombs[i][1] - bombs[p][1]) ** 2 <= bombs[p][2] ** 2:
                        result.append(i)
                        root.append(i)
            return result

        for i in range(n):
            count = len(search_one(bombs, i))
            max_count = max(max_count, count)

        return max_count