import copy
import unittest
import random
from unique_linked_list import UniqueLinkedList


one_test = [1]
two_test = ["a", "vv"]
small_test_wrong = [5, 2, 1, 6, 10000, 2, 4]
small_test = [5, 2, 1, 6, 10000, 4]
one_hundred_test = list(range(100))
one_million_test = list(range(1000000))


def get_all_elements_del_last(linked_list: UniqueLinkedList):
    list_size = linked_list.size
    return [linked_list.delete_last() for _ in range(list_size)]


def get_linked_list_by_list(element_list: list):
    linked_list = UniqueLinkedList()
    for element in element_list:
        linked_list.add(element, element)
    return linked_list


class TestUniqueLinkedListMethods(unittest.TestCase):

    def test_add_delete_last_default(self):

        def get_del_result(element_list: list):
            return get_all_elements_del_last(get_linked_list_by_list(element_list))

        self.assertEqual(get_del_result(one_test), one_test)
        self.assertEqual(get_del_result(two_test), two_test)
        with self.assertRaises(AssertionError):
            get_del_result(small_test_wrong)
        self.assertEqual(get_del_result(small_test), small_test)
        self.assertEqual(get_del_result(one_hundred_test), one_hundred_test)
        self.assertEqual(get_del_result(one_million_test), one_million_test)

    def test_size_default(self):
        one_linked_list = get_linked_list_by_list(one_test)
        self.assertEqual(one_linked_list.size, 1)
        one_linked_list.delete_last()
        self.assertEqual(one_linked_list.size, 0)
        two_linked_list = get_linked_list_by_list(two_test)
        self.assertEqual(two_linked_list.size, 2)
        two_linked_list.delete_last()
        self.assertEqual(two_linked_list.size, 1)

    def test_delete_node(self):
        one_linked_list = get_linked_list_by_list(one_test)
        one_linked_list.delete_node(1)
        self.assertEqual(get_all_elements_del_last(one_linked_list), [])

        two_linked_list = get_linked_list_by_list(two_test)
        two_linked_list.delete_node("vv")
        self.assertEqual(get_all_elements_del_last(two_linked_list), ["a"])

        copy_hundred_list = copy.deepcopy(one_hundred_test)
        hundred_linked_list = get_linked_list_by_list(one_hundred_test)
        shuffled_hundred_list = copy.deepcopy(one_hundred_test)
        random.shuffle(shuffled_hundred_list)
        for removing_element in shuffled_hundred_list:
            copy_hundred_list.remove(removing_element)
            hundred_linked_list.delete_node(removing_element)
            self.assertEqual(list(hundred_linked_list), copy_hundred_list[::-1])


if __name__ == '__main__':
    unittest.main()
