"""
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
"""

"""
思路：
    如果x-y油不够的话，那么x-y之间的任意点i-y也不会够。
    所以可以一次遍历。
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        have = gas[0] - cost[0]
        minnum = [have, 0]
        for i in range(1, len(gas)):
            have = gas[i] - cost[i] + have
            if have <= minnum[0]:
                minnum = [have, i]
        if have < 0:
            return -1
        return (minnum[1] + 1) % len(gas)