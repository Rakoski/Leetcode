# Definition for singly-linked list.
# Import Optional (I have never ever used Optional in Python lol)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            arr = cur.next
            cur.next = prev
            prev = cur
            cur = arr
        return prev
