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
        if not head or not head.next:
            return head
        
        def sortSubList(subHead, subTail):
            # 左开右闭
            print('subhead: ', subHead)
            print('subTail: ', subTail)
            if subTail is None or subHead.next == subTail:
                return
            
            subHeadNext = subHead.next
            if subHeadNext.next == subTail:
                if subTail.val > subHeadNext.val:
                    subHead.next = subTail
                    subHeadNext.next = subTail.next
                    subTail.next = subHeadNext
                return
            
            # 快慢指针
            low, fast = subHead, subHead
            while True:
                if fast == subTail or fast.next == subTail:
                    break
                low = low.next
                fast = fast.next.next
            
            if fast != subTail:
                fast = fast.next
            
            sortSubList(subHead, low)
            sortSubList(low, fast)

        preHead = ListNode(val=-1, next=head)

        low, fast = preHead, preHead
        while fast.next and fast.next.next:
            low = low.next
            fast = fast.next.next

        if fast.next:
            fast = fast.next
            low = low.next
        # print('low: ', low)
        # print('fast: ', fast)
        sortSubList(preHead, low)
        sortSubList(low, fast)
        print(head)
        return head
               