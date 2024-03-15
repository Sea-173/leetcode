"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""

"""
思路总结
    合并K个升序链表，思想基于合并2个有序链表，
    采用分治法，每次合并两个，一直迭代到合并为一个
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None
        if len(lists) < 2:
            return lists[0]
        def merge2Lists(head1, head2):
            L, R = head1, head2
            head = ListNode()
            cur = head
            while L and R:
                if L.val < R.val:
                    cur.next = L
                    L = L.next
                    cur = cur.next
                else:
                    cur.next = R
                    R = R.next
                    cur = cur.next
            if L:
                cur.next = L
            if R:
                cur.next = R
            return head.next
        
        stack = lists
        count = 0
        while stack:
            head1 = stack.pop(0)
            if stack:
                head2 = stack.pop(0)
                head = merge2Lists(head1, head2)
                stack.append(head)
            else:
                break
        return head1
        