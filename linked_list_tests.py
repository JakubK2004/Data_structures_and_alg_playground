import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_add_node_as_tail(self):
        self.list.add_node_as_tail(1)
        self.assertEqual(self.list.values, [1])

    def test_add_node_as_head(self):
        self.list.add_node_as_head(2)
        self.assertEqual(self.list.values, [2])

    def test_insert_node(self):
        self.list.append_multiple_nodes([1, 3])
        self.list.insert_node(1, 2)
        self.assertEqual(self.list.values, [1, 2, 3])

    def test_delete_node(self):
        self.list.append_multiple_nodes([1, 2, 3])
        self.list.delete_node(1)
        self.assertEqual(self.list.values, [1, 3])

    def test_search_by_index(self):
        self.list.append_multiple_nodes([1, 2, 3])
        self.assertEqual(self.list.search_by_index(1), 2)

    def test_search_by_value(self):
        self.list.append_multiple_nodes([1, 2, 3])
        self.assertEqual(self.list.search_by_value(2), 1)
        self.assertEqual(self.list.search_by_value(4), -1)

    def test_delete_by_value(self):
        self.list.append_multiple_nodes([1, 2, 3])
        self.list.delete_by_value(2)
        self.assertEqual(self.list.values, [1, 3])

    def test_reverse_list(self):
        self.list.append_multiple_nodes([1, 2, 3])
        self.list.reverse_list()
        self.assertEqual(self.list.values, [3, 2, 1])

    def test_clear_list(self):
        self.list.append_multiple_nodes([1, 2, 3])
        self.list.clear_list()
        self.assertEqual(self.list.values, [])

    def test_sort_list(self):
        self.list.append_multiple_nodes([3, 1, 2])
        self.list.sort_list()
        self.assertEqual(self.list.values, [1, 2, 3])

    def test_remove_duplicates(self):
        self.list.append_multiple_nodes([1, 2, 2, 3])
        self.list.remove_duplicates()
        self.assertEqual(self.list.values, [1, 2, 3])

    def test_find_middle(self):
        self.list.append_multiple_nodes([1, 2, 3, 4, 5])
        self.assertEqual(self.list.find_middle(), 3)
        self.list.append_multiple_nodes([6])
        self.assertEqual(self.list.find_middle(), 4)


if __name__ == '__main__':
    unittest.main()
