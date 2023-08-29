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
        node_que_ta_agora_na_contagem = self.head
        count = 0

        while node_que_ta_agora_na_contagem is not None:
            if count == index:
                return node_que_ta_agora_na_contagem.val
            node_que_ta_agora_na_contagem = node_que_ta_agora_na_contagem.next
            count += 1

        return -1

    # Add a node of value val before the first element of the linked list.
    # After the insertion, the new node will be the first node of the linked list.
    def add_at_head(self, val: int) -> None:
        nova_head = DoubleNode(val)

        if not self.head:
            self.head = nova_head
            self.tail = nova_head

        else:
            nova_head.next = self.head
            self.head.prev = nova_head
            self.head = nova_head

    # Append a node of value val as the last element of the linked list.
    def add_at_tail(self, val: int) -> None:
        new_tail = DoubleNode(val)

        if not self.head:
            self.head = new_tail
            self.tail = new_tail

        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

    # Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list,
    # the node will be appended to the end of the linked list.
    # If index is greater than the length, the node will not be inserted.
    def add_at_index(self, index: int, val: int) -> None:
        if index < 0:
            return  # não podem ter indices negativos

        new_node = DoubleNode(val)

        if index == 0:  # adding at the head

            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node

            if not self.tail:  # se não tiver nada no tail, isto é, se tiver sendo criada uma nova lista
                self.tail = new_node

        else:
            cur = self.head
            count = 0
            while cur:
                if count == (index - 1):

                    new_node.next = cur.next  # inserting a new node after the index - 1 node
                    new_node.prev = cur  # the prev pointer is set to the node at index - 1 position

                    if cur.next:  # checking if we're at the middle of the list or at the end
                        cur.next.prev = new_node
                        # if we're in the middle, we have to update the 'prev' pointer of the next node to set to
                        # the node we have just inserted in the middle of the list

                    else:
                        self.tail = new_node
                        # if we're in the end of the list, mark the 'tail' pointer to our new node

                    cur.next = new_node
                    break

                cur = cur.next  # esse cur.next seria a node em que o índice está
                count += 1

    # Deletes the indexth node in the linked list, if the index is valid.
    def delete_at_index(self, index: int) -> None:
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
