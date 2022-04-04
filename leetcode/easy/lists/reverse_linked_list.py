from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node = None
    while head:
        head.next, head, previous_node = previous_node, head.next, head
    return previous_node


node5 = ListNode(val=5)
node4 = ListNode(val=4, next=node5)
node3 = ListNode(val=3, next=node4)
node2 = ListNode(val=2, next=node3)
head = ListNode(val=1, next=node2)

reverseList(head)
