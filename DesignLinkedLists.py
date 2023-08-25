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

    # Append a node of value val as the last element of the linked list.
    def addAtTail(self, val: int) -> None:
        new_tail = DoubleNode(val)

        if not self.tail:
            self.head = new_tail
            self.tail = new_tail

        else:
            new_tail.prev = self.tail  # o node de antes da onde será colocado o novo node é o tail
            self.tail.next = new_tail
            self.tail = new_tail

    # Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list,
    # the node will be appended to the end of the linked list.
    # If index is greater than the length, the node will not be inserted.
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return  # não podem ter indices negativos

        new_node = DoubleNode(val)

        if index == 0:  # adding at the head

            new_node.next = self.head  # declarei aonde vai ser colocado a nova node
            if self.head:  # se tiver algo no node da head
                self.head.prev = new_node
            self.head = new_node

            if not self.tail:  # se não tiver nada no tail, isto é, se tiver sendo criada uma nova lista
                self.tail = new_node

        else:
            cur = self.head
            count = 0
            while cur:
                if count == (index - 1):

                    new_node.next = cur.next  # conectando o node no meio da lista, no index
                    new_node.prev = cur  # new_node conecta aonde o current (do while) parou por causa do (index - 1)

                    if cur.next:  # se tiver algo depois do novo node
                        cur.next.prev = new_node  # faz o update em si. This step updates the prev pointer of cur.next
                        # to point to the new_node. Now, cur.next is the node following the new_node.

                    else:  # se não tiver nada depois da onde parou o índice, isto é, estamos na última posição
                        self.tail = new_node  # o tail agora é o new_node

                    cur.next = new_node  # o tal da posição do índice agora é o new_node
                    break

                cur = cur.next  # esse cur.next seria a node em que o índice está
                count += 1


    # Deletes the indexth node in the linked list, if the index is valid.
    def deleteAtIndex(self, index: int) -> None:
        # no caso, eu teria que chegar na node, e, se caso for o head ou o tail, terei que fazer o update

        if index < 0:
            return

        cur = self.head
        count = 0
        while cur:
            if count == index:
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev

                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next

                break

            cur = cur.next
            count += 1

        # esse foi o único que eu consegui fazer mais ou menos

