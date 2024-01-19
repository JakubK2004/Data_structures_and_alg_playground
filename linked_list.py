class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self._head = None
        if values is not None:
            self.append_multiple_nodes(values)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self._head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self._head
        while current:
            yield current
            current = current.next

    @property
    def values(self):
        return [node.value for node in self]

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = Node(value, self._head)

    @head.deleter
    def head(self):
        if self._head:
            self._head = self._head.next

    def add_node_as_tail(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node

    def append_multiple_nodes(self, values):
        for value in values:
            self.add_node_as_tail(value)

    def add_node_as_head(self, value):
        self._head = Node(value, self._head)

    def insert_node(self, index, value):
        if index < 0 or index > len(self):
            raise IndexError("Index out of bounds")

        if index == 0:
            self.add_node_as_head(value)
            return

        current = self._head
        for _ in range(index - 1):
            current = current.next
            if current is None:
                raise IndexError("Index out of bounds")

        current.next = Node(value, current.next)

    def delete_node(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of bounds")

        if index == 0:
            del self.head
            return

        current = self._head
        for _ in range(index - 1):
            current = current.next
            if current is None or current.next is None:
                raise IndexError("Index out of bounds")

        current.next = current.next.next

    def delete_by_value(self, value):
        if self._head and self._head.value == value:
            self._head = self._head.next
            return
        current = self._head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search_by_index(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of bounds")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.value

    def search_by_value(self, value):
        current = self._head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def reverse_list(self):
        prev = None
        current = self._head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self._head = prev

    def clear_list(self):
        self._head = None

    def sort_list(self):
        if self._head is None or self._head.next is None:
            return
        sorted_bool = False
        while not sorted_bool:
            sorted_bool = True
            current = self._head
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    sorted_bool = False
                current = current.next

    def remove_duplicates(self):
        current = self._head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next

    def find_middle(self):
        slow = self._head
        fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None
