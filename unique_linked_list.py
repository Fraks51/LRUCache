class UniqueLinkedList:

    class Node:

        def __init__(self, value, key=None, forward=None, back=None):
            self.value = value
            self.key = key
            self.forward = forward
            self.back = back

    def __init__(self):
        self._tail = self.Node(None)
        self._head = self.Node(None, forward=self._tail)
        self._tail.back = self._head
        self._dict = dict()
        self.size = 0

    def add(self, key, value):
        assert key is not None, "Key can't to be None"
        assert key not in self._dict, f"All keys should be unique in UniqueLinkedList, element with key:{key} was added"

        self.size += 1
        first_node = self._head.forward
        new_node = self.Node(value, key=key, forward=first_node, back=self._head)
        self._head.forward = new_node
        first_node.back = new_node
        self._dict[key] = new_node

    def delete_last(self):
        assert self.size != 0, "Can't remove node from empty linked list"

        self.size -= 1
        new_last_node = self._tail.back.back
        result = self._tail.back.value
        self._dict.pop(self._tail.back.key)
        del self._tail.back
        new_last_node.forward = self._tail
        self._tail.back = new_last_node
        return result

    def _get_node(self, key):
        assert key is not None, "Key can't to be None"
        return self._dict[key] if key in self._dict else None

    def get_value(self, key):
        assert key is not None, "Key can't to be None"
        return self._dict[key].value if key in self._dict else None

    def delete_node(self, key):
        assert key is not None, "Key can't to be None"
        assert self.size != 0, "Can't remove node from empty linked list"
        assert key in self._dict, f"No node with this key {key}"

        node = self._get_node(key)

        self.size -= 1
        back_node = node.back
        forward_node = node.forward
        self._dict.pop(node.key)
        del node
        back_node.forward = forward_node
        forward_node.back = back_node

    def __len__(self):
        return self.size

    def __iter__(self):
        return UniqueLinkedListIterator(self)


class UniqueLinkedListIterator:
    def __init__(self, linked_list: UniqueLinkedList):
        self._size = linked_list.size
        self._index = -1
        self._tmp_node = linked_list._head

    def __next__(self):
        if self._index + 1 < self._size:
            self._index += 1
            self._tmp_node = self._tmp_node.forward
            return self._tmp_node.value

        # End of Iteration
        raise StopIteration
