from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if not list1 or not list2:
        return list1 or list2

    if list1.val <= list2.val:
        root = ListNode(list1.val, None)

        root.next = mergeTwoLists(list1.next, list2)
    else:
        root = ListNode(list2.val, None)
        root.next = mergeTwoLists(list1, list2.next)
    return root


# node1_3 = ListNode(val=4)
# node1_2 = ListNode(val=2, next_val=node1_3)
# node1_1 = ListNode(val=1, next_val=node1_2)
#
# node2_3 = ListNode(val=4)
# node2_2 = ListNode(val=3, next_val=node2_3)
# node2_1 = ListNode(val=1, next_val=node2_2)

# node1_3 = ListNode(val=4)
# node1_2 = ListNode(val=2, next_val=node1_3)
# node1_1 = ListNode(val=1, next_val=node1_2)
#
# node2_1 = ListNode(val=5)

# node2_3 = ListNode(val=4)
# node2_2 = ListNode(val=2, next_val=node2_3)
# node2_1 = ListNode(val=1, next_val=node2_2)
#
# node1_1 = ListNode(val=5)

node2_2 = ListNode(val=3)
node2_1 = ListNode(val=-9, next=node2_2)

node1_1 = ListNode(val=7)
node1_1 = ListNode(val=5, next=node1_1)

mergeTwoLists(node1_1, node2_1)
