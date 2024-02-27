"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""

"""
思路总结：
    注意需要一个pre指针，用于记录当前节点的前一个节点
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre