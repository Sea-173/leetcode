class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = {}
        nodes[0] = ListNode(val=0, next=head)
        cur = head
        cur_index = 1
        while cur is not None:
            nodes[cur_index] = cur
            cur_index += 1
            cur = cur.next
        
        del_node_index = cur_index - n

        nodes[cur_index] = None

        nodes[del_node_index-1].next = nodes[del_node_index+1]
        del nodes[del_node_index]
        return nodes[0].next