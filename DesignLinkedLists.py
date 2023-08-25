class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    def get(self, index: int) -> int:
        cur = self.head
        count = 0

        while cur is not None:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1

        return -1

    # Add a node of value val before the first element of the linked list.
    # After the insertion, the new node will be the first node of the linked list.
    def addAtHead(self, val: int) -> None:
        new_head = DoubleNode(val)  # inicializando a new_head com seu valor (val)

        # In my first attempt, I forgot the case that the node could be empty
        if not self.head:
            self.head = new_head
            self.tail = new_head

        # I had done this already (to an extent I guess)
        else:
            new_head.next = self.head  # o próximo (node 2) seria a head, por enquanto
            self.head.prev = new_head  # adicionada a nova node
            self.head = new_head  # a nova node (new_head) agora é a nova head

    def addAtTail(self, val: int) -> None:

    def addAtIndex(self, index: int, val: int) -> None:

    def deleteAtIndex(self, index: int) -> None: