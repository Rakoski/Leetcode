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
            dummy = cur.next
            cur.next = prev
            prev = cur
            cur = dummy
        return prev

    # enquanto o current não for null, aka, enquanto não chegar na última nodelist
    # o dummy vai ser o de agora.próximo
    # agora.próximo vai ser o de antes (pra continuar o loop)
    # o de antes vai ser o de agora (também pra continuar o loop)
    # e o de agora vai virar o dummy (pro loop continuar)
    # retorne a nodelist criada reversamente, que no caso, é o prev (previous)
