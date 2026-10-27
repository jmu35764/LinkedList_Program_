from Node import node
from SinglyLinkedList import SinglyLinkedList

sl1 = SinglyLinkedList()

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



