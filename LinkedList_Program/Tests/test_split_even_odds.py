import unittest
from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import node
from split_evens_odds import SplitEvensOdds

class Test_SplitEvensOdds(unittest.TestCase):
    
    def test_even_and_odd(self):
        sl1 = SplitEvensOdds()
        values = [1, 2, 3, 4, 5, 6]
        even_numbers = [num for num in numbers if num % 2 == 0]
        sl1.build_list_forward(values)

        evens, odds = sl1.split_even_odd()

        self.assertEqual(list(evens), even_numbers)
        self.assertEqual(list(odds), [1, 3, 5])





