from SinglyLinkedList import node
from SinglyLinkedList import SinglyLinkedList
from split_evens_odds import SplitEvensOdds

sl1 = SinglyLinkedList()

n1 = node()
n1.data = 5

#*** FORWARD AND BACKWARD LIST CONSTRUCTION ***
values = [10, 20, 30, 40, 50]
print("*** FORWARD AND BACKWARD LIST CONSTRUCTION ***")
print(f"The following values {values} will be added to a list")
print(f"In the first list they will be added in forward order")
sl2 = SinglyLinkedList()
sl2.build_list_forward(values)
print(sl2)

print(f"\n In the next list they will be added in reverse order")
sl3 = SinglyLinkedList()
sl3.build_list_backward(values)
print(sl3)

#*** INSERTING AND REMOVING VALUES ***
print("\n INSERTING AND REMOVING VALUES")
print("Now we will start a new list")
sl4 = SinglyLinkedList()
sl4.build_list_forward([1, 3, 5, 7, 9])
print(sl4)

print("\nFirst we will remove the number 3 from the list")
sl4.remove(3)
print(sl4)

print("\nNow we will add a 7 where the 3 used to be")
sl4.insert_after(1, 7)
print(sl4)

print("\nNext we will add a 7 to the head and tail of the list")
sl4.append(7)
sl4.prepend(7)
print(sl4)

print("\nNow we will remove all 7's from the list")
sl4.remove_all(7)
print(sl4)

#*** CREATING AND SPLITTING LISTS ***
print("\n*** CREATING AND SPLITTING LISTS")
print("Now we will create a list that will be split into two lists")
print("The list will be split into an even list and an odd list")
sl5 = SplitEvensOdds()
values_01 = [1, 2, 3, 4, 5, 6]
sl5.build_list_forward(values_01)

print("List before split\n")
print(sl5)
evens, odds = sl5.split_even_odd()

print(f"Evens:  {evens}")
print(f"Odds:   {odds}")

print("\nList after split: ")
print(sl5)

print("\nAfter the even and odd lists are made, we can still make changes to them")
print("Now, I will add a 2 to the end of the evens list")
evens.append(2)
print(evens)

print("\nNow I will remove the 5 from the odds list")
odds.remove(5)
print(odds)

