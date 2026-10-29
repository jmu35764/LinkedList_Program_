from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import node

class SplitEvensOdds(SinglyLinkedList):
    def __init__(self)
        super().__init__()
        self._field = field

    def split_even_odd(self)
        if self.is_empty() = True:
            raise ValueError{"List is empty"}

        even_list, odd_list = SinglyLinkedList()

        #Set Current Cursor to head
        current = self._head

        #Clear the orginal list
        self._head = None
        self._tail = None
        self._count = 0

        while(current)
            next_node = current.next
            current.next  = None
            
            if current.data % 2 == 0:
                if even_list.tail is None:
                    even_list.head = even_list.tail = current
                else:
                    even_list._tail.next = current
                    even_list._tail = current
                even_list.count += 1
            else: 
                if odd_list.tail is None:
                    odd_list.head = even_list.tail = current
                else:
                    odd_list._tail.next = current
                    odd_list._tail = current
                odd_list.count += 1

            current = next_node

        return even_list, odd_list




        

    pass




