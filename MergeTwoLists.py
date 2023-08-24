from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next  # updating the pointer for l1
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # updating the tail pointer for either conditions

        # clean code!
        if l1 is not None:
            tail.next = l1
        elif l2 is not None:
            tail.next = l2

        return dummy.next
