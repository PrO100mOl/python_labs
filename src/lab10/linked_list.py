from __future__ import annotations

from typing import Any, Iterable, Iterator


class Node:

    __slots__ = ("value", "next")

    def __init__(self, value: Any, next: Node | None = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str: 
        return f"Node({self.value!r})"


class SinglyLinkedList:

    def __init__(self, values: Iterable[Any] | None = None) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0
        if values is not None:
            for value in values:
                self.append(value)

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of range")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        prev = self._node_at(idx - 1)
        new_node = Node(value, prev.next)
        prev.next = new_node
        self._size += 1

    def remove(self, value: Any) -> None:
        if self.head is None:
            raise ValueError("List is empty")

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        prev = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                prev.next = current.next
                if current is self.tail:
                    self.tail = prev
                self._size -= 1
                return
            prev, current = current, current.next

        raise ValueError(f"{value!r} not found in list")

    def _node_at(self, idx: int) -> Node:
        current = self.head
        for _ in range(idx):
            assert current is not None 
            current = current.next
        assert current is not None
        return current

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int: 
        return self._size

    def __repr__(self) -> str:  
        return f"SinglyLinkedList([{', '.join(repr(v) for v in self)}])"

    def __str__(self) -> str: 
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value!r}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)


if __name__ == "__main__":
    ll = SinglyLinkedList([1, 2, 4])
    print("Initial:", ll)
    ll.prepend(0)
    ll.append(5)
    ll.insert(3, 3)
    print("After modifications:", ll)
    ll.remove(2)
    print("After removing 2:", ll)
    print("Length:", len(ll))
    print("Iterating:", list(ll))
