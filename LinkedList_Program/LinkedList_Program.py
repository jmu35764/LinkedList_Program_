from SinglyLinkedList import node
from SinglyLinkedList import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

"""sl1 = SinglyLinkedList()

n1 = node()
n1.data = 5

sl1.append(5)
sl1.append(6)
sl1.append(11)

print(sl1._head.data)
print(sl1._tail.data)
sl1.__iter__()

sl1.insert_after(6, 8)
sl1.__iter__()

#sl1.insert_after(7, 9)
sl1.remove(5)
sl1.__iter__()

print(sl1.contains(6))
print(sl1.contains(11))

sl2 = SinglyLinkedList()
sl2.build_list_forward([1, 2, 3, 4, 5])
sl2.__iter__()
sl3 = SinglyLinkedList()
sl3.build_list_backward([6, 7, 8, 7, 10])
sl3.__iter__()
sl3.remove_all(7)
sl3.__iter__()
sl2.remove_all(7)
print(sl2)"""

sl4 = SplitEvensOdds()
sl4.build_list_forward([1, 2, 2, 2, 3])
sl4.__iter__()
list(sl4.__iter__())
evens, odds = sl4.split_even_odd()

print(f"Evens:  {evens}")
print(f"Odds:   {odds}")
print(sl4.is_empty())


