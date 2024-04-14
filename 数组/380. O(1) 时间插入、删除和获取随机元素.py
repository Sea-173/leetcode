"""
实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
"""

class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.nums = []


    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.set:
            indice = self.set[val]
            self.set[self.nums[-1]] = indice
            self.nums[indice], self.nums[-1] = self.nums[-1], self.nums[indice]
            self.nums.pop()
            del self.set[val]
            return True
        return False


    def getRandom(self) -> int:
        return choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()