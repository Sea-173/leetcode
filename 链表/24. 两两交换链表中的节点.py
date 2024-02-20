# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        cur = head

        while cur and cur.next:
            first = cur
            second = cur.next
            temp = first.val
            first.val = second.val
            second.val = temp
            cur = second.next
        return head