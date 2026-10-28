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

    def test_insert_after(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)
        sl1.insert_after(6, 8)
        self.assertTrue(sl1.contains(8))

    def test_is_empty(self):
        sl1 = SinglyLinkedList()
        self.assertTrue(sl1.is_empty())
        sl1.append(5)
        self.assertFalse(sl1.is_empty())

    def test_remove(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)
        sl1.remove(6)
        self.assertFalse(sl1.contains(6))

    def test_remove_nonexistent(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)
        with self.assertRaises(ValueError):
            sl1.remove(10)
        self.assertEqaul(sl1._count, 3)  # Ensure the count remains unchanged

if __name__ == '__main__':
    unittest.main()