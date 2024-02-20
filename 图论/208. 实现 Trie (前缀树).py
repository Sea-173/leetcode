"""
题目描述：
    Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

    请你实现 Trie 类：

    Trie() 初始化前缀树对象。
    void insert(String word) 向前缀树中插入字符串 word 。
    boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
    boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
"""

"""
思路总结：
    这道题分类在图论里面，但是没啥关系，很简单。
    首先想到26个英文字母有限，因此构建一个简单的多叉树就可以满足题目需求。
    在多叉树的基础上，需要增加isFinal变量来表明从root到当前节点是否为一个单词，区分插入的apple和app。
    如果把链表改为直接创建26个英文字符的字典，可以空间换时间。
"""

class Trie:
    def __init__(self, val=-1, next=[], isFinal=False):
        self.val = val
        self.next = []
        self.isFinal = isFinal

    def insert(self, word: str) -> None:
        cur = self
        for w in word:
            tf = False
            for cn in cur.next:
                if cn.val == w:
                    cur = cn
                    tf = True
                    break
            if not tf:
                new_next = Trie(val=w, next=[], isFinal=False)
                cur.next.append(new_next)
                cur = new_next
                # print('new_next: ', new_next.val, new_next.next, new_next.isFinal)
        cur.isFinal = True
        return

    def search(self, word: str) -> bool:
        cur = self
        for w in word:
            # print('cur: ', cur.val, len(cur.next), cur.isFinal)
            tf = False
            for cn in cur.next:
                if w == cn.val:
                    cur = cn
                    tf = True
                    break
            if not tf:
                return False
        # print('cur: ', cur.val, len(cur.next), cur.isFinal)
        return cur.isFinal


    def startsWith(self, prefix: str) -> bool:
        cur = self
        for w in prefix:
            tf = False
            for cn in cur.next:
                if w == cn.val:
                    cur = cn
                    tf = True
                    break
            if not tf:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)