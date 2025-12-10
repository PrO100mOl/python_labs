from collections import deque
from typing import Any, Iterable


class Stack:
    def __init__(self, items: Iterable[Any] | None = None) -> None:
        self._data: list[Any] = list(items) if items is not None else []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self) -> Any | None:
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int: 
        return len(self._data)

    def __repr__(self) -> str: 
        return f"Stack({self._data!r})"


class Queue:

    def __init__(self, items: Iterable[Any] | None = None) -> None:
        self._data: deque[Any] = deque(items or [])

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data.popleft()

    def peek(self) -> Any | None:
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)!r})"


if __name__ == "__main__":
    print("--- Stack demo ---")
    stack = Stack([1, 2, 3])
    print("Initial:", stack)
    stack.push(4)
    print("After push:", stack)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Final:", stack)

    print("\n--- Queue demo ---")
    queue = Queue(["a", "b", "c"])
    print("Initial:", queue)
    queue.enqueue("d")
    print("After enqueue:", queue)
    print("Peek:", queue.peek())
    print("Dequeue:", queue.dequeue())
    print("Final:", queue)
