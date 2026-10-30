import unittest
from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import node
from split_evens_odds import SplitEvensOdds

class Test_SplitEvensOdds(unittest.TestCase):
    
    def test_even_and_odd(self):
        sl1 = SplitEvensOdds()
        values = [1, 2, 3, 4, 5, 6]
        even_numbers = [value for value in values if value % 2 == 0]
        odd_numbers = [value for value in values if value % 2 != 0]
        sl1.build_list_forward(values)

        evens, odds = sl1.split_even_odd()

        self.assertEqual(list(evens), even_numbers)
        self.assertEqual(list(odds), odd_numbers)

        self.assertEqual(len(evens), 3)
        self.assertEqual(len(odds), 3)
        self.assertEqual(len(evens) + len(odds), len(values) )

        self.assertTrue(evens._tail.next is None)
        self.assertTrue(odds._tail.next is None)

        self.assertTrue(sl1.is_empty())

    def test_all_even(self):
        sl1 = SplitEvensOdds()
        values = [2, 4, 6, 8]
        even_numbers = [value for value in values if value % 2 == 0]
        odd_numbers = [value for value in values if value % 2 != 0]
        sl1.build_list_forward(values)

        evens, odds = sl1.split_even_odd()

        self.assertEqual(list(evens), even_numbers)
        self.assertEqual(list(odds), odd_numbers)

        self.assertEqual(len(evens), 4)
        self.assertEqual(len(odds), 0)
        self.assertEqual(len(evens) + len(odds), len(values) )

        self.assertTrue(evens._tail.next is None)
        self.assertTrue(odds.is_empty())

        self.assertTrue(sl1.is_empty())

    def test_all_odd(self):
        sl1 = SplitEvensOdds()
        values = [1, 3, 5, 7]
        even_numbers = [value for value in values if value % 2 == 0]
        odd_numbers = [value for value in values if value % 2 != 0]
        sl1.build_list_forward(values)

        evens, odds = sl1.split_even_odd()

        self.assertEqual(list(evens), even_numbers)
        self.assertEqual(list(odds), odd_numbers)

        self.assertEqual(len(evens), 0)
        self.assertEqual(len(odds), 4)
        self.assertEqual(len(evens) + len(odds), len(values) )

        self.assertTrue(evens.is_empty())
        self.assertTrue(odds._tail.next is None)

        self.assertTrue(sl1.is_empty())

    def test_single_even(self):
        sl1 = SplitEvensOdds()
        values = [4]
        even_numbers = [value for value in values if value % 2 == 0]
        odd_numbers = [value for value in values if value % 2 != 0]
        sl1.build_list_forward(values)

        evens, odds = sl1.split_even_odd()

        self.assertEqual(list(evens), even_numbers)
        self.assertEqual(list(odds), odd_numbers)

        self.assertEqual(len(evens), 1)
        self.assertEqual(len(odds), 0)
        self.assertEqual(len(evens) + len(odds), len(values) )

        self.assertTrue(evens._tail.next is None)
        self.assertTrue(odds.is_empty())

        self.assertTrue(sl1.is_empty())

    def test_single_odd(self):
        sl1 = SplitEvensOdds()
        values = [5]
        even_numbers = [value for value in values if value % 2 == 0]
        odd_numbers = [value for value in values if value % 2 != 0]
        sl1.build_list_forward(values)

        evens, odds = sl1.split_even_odd()

        self.assertEqual(list(evens), even_numbers)
        self.assertEqual(list(odds), odd_numbers)

        self.assertEqual(len(evens), 0)
        self.assertEqual(len(odds), 1)
        self.assertEqual(len(evens) + len(odds), len(values) )

        self.assertTrue(evens.is_empty())
        self.assertTrue(odds._tail.next is None)

        self.assertTrue(sl1.is_empty())





