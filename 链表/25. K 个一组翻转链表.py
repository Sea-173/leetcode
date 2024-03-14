"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""

"""
思路总结
    根据题目思路，每k个节点翻转一次，很自然能想到反转链表的子函数（详见第206题）
    需要对子函数进行修改，输入为反转链表+前后多两个节点，因为需要对这两个节点的next进行反转，这一步很重要
    然后使用pre指针表示子链表头，cur指针进行遍历，没k个翻转即可。
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseK(pre_head, tail):
            # 不反转tail
            head = pre_head.next
            cur = head
            pre = pre_head
            while cur != tail:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            pre_head.next = pre
            head.next = tail
            return head

        dummyHead = ListNode(0, head)
        pre, cur = dummyHead, head
        count = 0
        while cur:
            count += 1
            if count % k == 0:
                tail = cur.next
                pre = reverseK(pre, tail)           
                cur = tail
            else:
                cur = cur.next
        return dummyHead.next

            

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()
s.reverseKGroup(head, 3)

cur = head
while cur is not None:
    print(cur.val)
    cur = cur.next