"""
题目描述：
    给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def mergeSort(left, right):
            dummyHead = ListNode(-1)
            cur = dummyHead

            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            if left:
                cur.next = left
            elif right:
                cur.next = right
            return dummyHead.next
        
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        dummyHead = ListNode(-1, head)
        k = 1
        while k < n:
            cur = dummyHead.next
            pre = dummyHead

            while cur:
                left = cur
                for i in range(1, k):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                if not cur.next:
                    pre.next = left
                    break

                right = cur.next
                cur.next = None
                cur = right
                for i in range(1, k):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                
                nxt = None
                if cur.next:
                    nxt = cur.next
                    cur.next = None
                cur = nxt

                pre.next = mergeSort(left, right)
                while pre.next:
                    pre = pre.next
            k *= 2
        return dummyHead.next

               