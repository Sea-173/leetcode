# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre_head = ListNode(val=0, next=head)
        stack_head = pre_head
        stack = []
        cur = head
        cur_index = 0

        def reversek(head, stack):
            if len(stack) == 1:
                stack.pop()
                return
            if len(stack) == 2:
                head.next = stack[1]
                stack[0].next = stack[1].next
                stack[1].next = stack[0]
                stack.pop()
                stack.pop(0)
                return
            head.next = stack[-1]
            stack[0].next = stack[-1].next
            stack[-1].next = stack[1]
            stack.pop()
            stack.pop(0)
            print(head.next, stack)
            reversek(head.next, stack)
            
        
        num = 0
        while cur is not None:
            if num == 5:
                break
            num += 1

            stack.append(cur)
            cur_index += 1
            print(cur)
            save_next = cur.next
            if cur_index % k == 0:
                next_head = stack[0]
                print('1', stack_head, '2', stack)
                reversek(stack_head, stack)
                
                stack = []
                stack_head = next_head
                print('1', stack_head, '2', stack)
            cur = save_next
            print()

        return pre_head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

s = Solution()
s.reverseKGroup(head, 3)

cur = head
while cur is not None:
    print(cur.val)
    cur = cur.next