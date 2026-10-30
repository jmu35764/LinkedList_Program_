import unittest
from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import node

class TestSinglyLinkedList(unittest.TestCase):
    
    def test_contains(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)

        self.assertTrue(sl1.contains(6))
        self.assertFalse(sl1.contains(10))
    
    def test_append(self):
        sl1 = SinglyLinkedList()
        self.assertTrue(sl1.is_empty())

        sl1.append(5)
        self.assertTrue(sl1.contains(5))

        sl1.append(6)
        self.assertTrue(sl1.contains(6))

        self.assertEqual(sl1._tail.data, 6)

    def test_prepend(self):
        sl1 = SinglyLinkedList()
        self.assertTrue(sl1.is_empty())

        sl1.prepend(5)
        self.assertTrue(sl1.contains(5))

        sl1.prepend(6)
        self.assertTrue(sl1.contains(6))

        self.assertEqual(sl1._head.data, 6)

    def test_build_list_forward(self):
        sl1 = SinglyLinkedList()
        values = [10, 20, 30, 40, 50]
        sl1.build_list_forward(values)
        self.assertEqual(list(sl1), values)
        self.assertEqual(len(sl1), 5)

    def test_build_list_backward(self):
        sl1 = SinglyLinkedList()
        values = [10, 20, 30, 40, 50]
        sl1.build_list_backward(values)
        self.assertEqual(list(sl1), values[::-1])
        self.assertEqual(len(sl1), 5)

    def test_len(self):
        sl1 = SinglyLinkedList()
        values = [1, 2, 3, 4, 5]
        sl1.build_list_forward(values)
        self.assertEqual(len(sl1), 5)

    def test_insert_after(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)
        sl1.insert_after(6, 8)
        self.assertTrue(sl1.contains(8))

    def test_insert_after_nonexistent(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)
        with self.assertRaises(ValueError):
            sl1.insert_after(10, 9)

    def test_is_empty(self):
        sl1 = SinglyLinkedList()
        self.assertTrue(sl1.is_empty())
        sl1.append(5)
        self.assertFalse(sl1.is_empty())

    def test_remove(self):
        values = [5, 6, 7, 11]
        sl1 = SinglyLinkedList()
        sl1.build_list_forward(values)

        sl1.remove(6)
        self.assertFalse(sl1.contains(6))

        sl1.remove(sl1._head.data)
        self.assertFalse(sl1.contains(5))

        sl1.remove(sl1._tail.data)
        self.assertFalse(sl1.contains(11))

        sl1.remove(7)
        self.assertTrue(sl1.is_empty())

    def test_remove_nonexistent(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)
        with self.assertRaises(ValueError):
            sl1.remove(10)
        self.assertEqual(sl1._count, 3)  # Ensure the count remains unchanged

if __name__ == '__main__':
    unittest.main()