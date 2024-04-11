"""
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right = 0,len(citations)
        while left<right:
            # +1 防止死循环
            mid = (left+right+1)>>1
            cnt = 0
            for v in citations:
                if v>=mid:
                    cnt+=1
            if cnt>=mid:
                # 要找的答案在 [mid,right] 区间内
                left=mid
            else:
                # 要找的答案在 [0,mid) 区间内
                right=mid-1
        return left