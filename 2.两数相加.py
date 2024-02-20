# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            cur_l1, cur_l2 = l1, l2
            isTen = False
            head = ListNode()
            result = head
            while cur_l1 or cur_l2:
                cur_value = 0
                if cur_l1:
                    cur_value += cur_l1.val
                    cur_l1 = cur_l1.next
                
                if cur_l2:  # 如果链表 l2 不为空
                    cur_value += cur_l2.val  # 将链表 l2 的当前节点的值加到 cur_value 上
                    cur_l2 = cur_l2.next  # 将 cur_l2 指针指向下一个节点

                if isTen:
                    isTen = False
                    cur_value += 1
                
                if cur_value >= 10:
                    isTen = True
                    cur_value -= 10
                
                result.val = cur_value
                if cur_l1 or cur_l2:
                    result.next = ListNode()
                    result = result.next
            if isTen:
                 result.next = ListNode(1)

            return head
                
