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

        def mergeSort(left: ListNode, right: ListNode) -> ListNode:
            '''合并两个已排序好的链表 left 和 right'''
            dummy_head = ListNode(-1)   # 虚拟节点
            tmp = dummy_head
            while left and right:       # left 和 right 均未遍历完
                if left.val <= right.val:
                    tmp.next = left
                    left = left.next
                else:
                    tmp.next = right
                    right = right.next
                tmp = tmp.next
            if left:                    # left 未遍历完
                tmp.next = left
            if right:                   # right 未遍历完
                tmp.next = right
            return dummy_head.next
        

        '''主程序开始'''
        n = 0               # 计算链表总长度
        tmp = head
        while tmp:
            tmp = tmp.next
            n += 1
        
        dummy_head = ListNode(-1, head)     # 虚拟节点，并指向head

        k = 1        # 子链表长度从 k=1 开始，逐步加倍（k=2*k）
        while k < n:
            # 依次合并两个长度为 k 的链表
            pre, cur = dummy_head, dummy_head.next
            while cur:

                '''第一个长度为 k 的链表，以left为头节点'''
                left = cur      
                for i in range(1, k):    # k-1 步即可走到 left 链表末尾
                    if cur.next:
                        cur = cur.next
                    else:       #  left链表长度未达到k
                        break
                
                # left链表长度未达到k也意味着后续right链表不存在，
                # 因此无需合并left和right链表，直接将left附加到上一个链表结尾，提前结束即可
                if not cur.next:
                    pre.next = left
                    break
                
                '''第二个长度为 k 的链表，以right为头节点'''
                right = cur.next    
                cur.next = None         # 断开left和right指代的链表
                cur = right
                for i in range(1, k):   # k-1 步即可走到 right 链表末尾
                    if cur and cur.next:
                        cur = cur.next
                    else:       #  right链表长度未达到k
                        break
                
                # 断开right链表与后续链表
                nxt = None
                if cur.next:
                    nxt = cur.next
                    cur.next = None
                cur = nxt   # cur继续指向下一个链表（如存在）

                '''合并 left 和 right 两个链表'''
                merged = mergeSort(left, right)
                pre.next = merged
                while pre.next:
                    pre = pre.next  # pre 移动到当前排序好的链表尾部

            k *= 2   # 子链表长度 x2
        
        return dummy_head.next

               