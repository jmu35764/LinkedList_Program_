from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import node

class SplitEvensOdds(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def split_even_odd(self):
        if self.is_empty() is True:
            raise ValueError("List is empty")

        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()

        #Set Current Cursor to head
        current = self._head

        #Clear the orginal list
        self._head = None
        self._tail = None
        self._count = 0

        while(current):
            next_node = current.next
            current.next  = None
            
            if current.data % 2 == 0:
                if even_list._tail is None:
                    even_list._head = even_list._tail = current
                else:
                    even_list._tail.next = current
                    even_list._tail = current
                even_list._count += 1
            else: 
                if odd_list._tail is None:
                    odd_list._head = odd_list._tail = current
                else:
                    odd_list._tail.next = current
                    odd_list._tail = current
                odd_list._count += 1

            current = next_node

        return even_list, odd_list


