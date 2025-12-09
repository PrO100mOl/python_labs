from collections import deque
from typing import Any, Iterable


class Stack:
    """Simple LIFO stack based on a Python list."""

    def __init__(self, items: Iterable[Any] | None = None) -> None:
        self._data: list[Any] = list(items) if items is not None else []

    def push(self, item: Any) -> None:
        """Place *item* on top of the stack."""
        self._data.append(item)

    def pop(self) -> Any:
        """Remove and return the top element.

        Raises:
            IndexError: if the stack is empty.
        """
        if not self._data:
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Return the top element without removing it.

        Returns ``None`` when the stack is empty.
        """
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        """Return ``True`` when the stack holds no elements."""
        return not self._data

    def __len__(self) -> int:  # pragma: no cover - trivial
        return len(self._data)

    def __repr__(self) -> str:  # pragma: no cover - representational
        return f"Stack({self._data!r})"


class Queue:
    """FIFO queue backed by :class:`collections.deque`."""

    def __init__(self, items: Iterable[Any] | None = None) -> None:
        self._data: deque[Any] = deque(items or [])

    def enqueue(self, item: Any) -> None:
        """Add *item* to the end of the queue."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Remove and return the element from the front.

        Raises:
            IndexError: if the queue is empty.
        """
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """Return the front element without removing it.

        Returns ``None`` when the queue is empty.
        """
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
        """Return ``True`` when the queue holds no elements."""
        return not self._data

    def __len__(self) -> int:  # pragma: no cover - trivial
        return len(self._data)

    def __repr__(self) -> str:  # pragma: no cover - representational
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
