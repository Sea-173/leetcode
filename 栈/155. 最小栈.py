"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。

"""

"""
思路1:
    使用一个辅助数组，数组存储的是有序数组指针，类似链表
    复杂度为O(n)，空间复杂度为O(n)，不好
"""

class MinStack1:

    def __init__(self):
        self.min_index = int(1e9)
        self.stack = []

    def push(self, val: int) -> None:
        if self.min_index >= int(1e9):
            self.stack.append([val, -1])
            self.min_index = 0
        else:
            cur_index = self.min_index
            if self.stack[cur_index][0] >= val:
                self.stack.append([val, cur_index])
                self.min_index = len(self.stack) - 1
            else:
                while True:
                    save_index = cur_index
                    cur_index = self.stack[cur_index][1]
                    if cur_index == -1 or self.stack[cur_index][0] >= val:
                        break
                if cur_index == -1:
                    self.stack.append([val, -1])
                    self.stack[save_index][1] = len(self.stack) - 1
                else:
                    self.stack.append([val, cur_index])
                    self.stack[save_index][1] = len(self.stack) - 1     
        return

    def pop(self) -> None:
        if len(self.stack) == 1:
            self.min_index = int(1e9)
            self.stack.pop()
            return
        if self.min_index == len(self.stack) - 1:
            self.min_index = self.stack[-1][1]
            self.stack.pop()
        else:
            cur_index = self.min_index
            while True:
                save_index = cur_index
                cur_index = self.stack[cur_index][1]
                if cur_index == len(self.stack) - 1:
                    break
            self.stack[save_index][1] = self.stack[cur_index][1]
            self.stack.pop()
        return


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[self.min_index][0]

"""
思路2:
    最小栈
    注意不需要保存太多信息，最小栈的核心思想是，每次push的时候，如果当前值小于等于最小栈的栈顶，则入栈，否则依旧入栈之前的值
"""
class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]