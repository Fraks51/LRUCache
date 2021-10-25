from unique_linked_list import UniqueLinkedList


class LRUCache:
    def __init__(self, max_size=100):
        assert max_size > 0, "Max size for cache should be more than one"

        self.max_size = max_size
        self.linked_list = UniqueLinkedList()

    def add(self, key, value):
        assert key is not None, "Key can't to be None"

        if self.linked_list.get_value(key) is None:
            self.linked_list.add(key, value)
            if self.linked_list.size > self.max_size:
                self.linked_list.delete_last()
        else:
            self.linked_list.delete_node(key)
            self.linked_list.add(key, value)

    def get(self, key):
        assert key is not None, "Key can't to be None"
        return self.linked_list.get_value(key)

    def __len__(self):
        return len(self.linked_list)
