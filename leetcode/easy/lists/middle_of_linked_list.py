from typing import Optional


class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next = next_val


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


node9 = ListNode(val=9, next_val=None)
node8 = ListNode(val=8, next_val=node9)
node7 = ListNode(val=7, next_val=node8)
node6 = ListNode(val=6, next_val=node7)
node5 = ListNode(val=5, next_val=node6)
node4 = ListNode(val=4, next_val=node5)
node3 = ListNode(val=3, next_val=node4)
node2 = ListNode(val=2, next_val=node3)
node1 = ListNode(val=1, next_val=node2)

res = middleNode(node1)
