# ЛР10 — Структуры данных: Stack, Queue и SinglyLinkedList

В работе реализованы базовые структуры данных на чистом Python и приведены простые примеры их использования и особенностей производительности.

## Теория в двух словах

| Структура | Ключевой принцип | Типичные операции | Сложность |
| --- | --- | --- | --- |
| Stack | LIFO (последний зашёл — первый вышел) | `push`, `pop`, `peek` | `O(1)` для добавления/удаления с вершины |
| Queue | FIFO (первый пришёл — первый вышел) | `enqueue`, `dequeue`, `peek` | `O(1)` для операций по краям при использовании `deque` |
| SinglyLinkedList | Цепочка узлов с ссылкой на следующий | `append`, `prepend`, `insert`, `remove` | Добавление в начало `O(1)`, в конец с хвостом `O(1)`, произвольная вставка/поиск `O(n)` |

*Главная идея бенчмарков:* операции, использующие конец списка (`Stack.push/pop`, `Queue.enqueue/dequeue` с `deque`) работают за константное время, а обход односвязного списка для вставки в середину/поиск растёт линейно. Для очередей на списках `list.pop(0)` оказывается заметно медленнее, поэтому `deque` предпочтительнее.

## Реализованные классы

- **`Stack`** (`structures.py`) — стек на базе `list` с методами `push`, `pop`, `peek`, `is_empty`, поддержкой `len()`. Пустой `pop` кидает `IndexError("Stack is empty")`, `peek` возвращает `None` при пустом стеке.
- **`Queue`** (`structures.py`) — очередь на базе `collections.deque` с методами `enqueue`, `dequeue`, `peek`, `is_empty`, поддержкой `len()`. Пустой `dequeue` кидает `IndexError("Queue is empty")`, `peek` возвращает `None` при пустой очереди.
- **`Node` / `SinglyLinkedList`** (`linked_list.py`) — односвязный список с головой, хвостом и счётчиком размера. Поддерживаются `append`, `prepend`, `insert(idx, value)`, `remove(value)`, итерация, `len()`, строковые представления через `__repr__` и «красивый» `__str__`. Удаление несуществующего значения приводит к `ValueError`.

## Примеры использования

### Stack / Queue

```bash
python - <<'PY'
from src.lab10.structures import Stack, Queue

stack = Stack([1, 2])
stack.push(3)
print(stack.pop())      # 3
print(stack.peek())     # 2
print(stack.is_empty()) # False

queue = Queue(["a"])
queue.enqueue("b")
print(queue.dequeue())  # a
print(queue.peek())     # b
print(len(queue))       # 1
PY
```

### SinglyLinkedList

```bash
python - <<'PY'
from src.lab10.linked_list import SinglyLinkedList

lst = SinglyLinkedList([1, 2, 3])
lst.prepend(0)
lst.append(4)
lst.insert(2, "X")
print(list(lst))        # [0, 1, 'X', 2, 3, 4]

lst.remove("X")
print(lst)              # [0] -> [1] -> [2] -> [3] -> [4] -> None
print(repr(lst))        # SinglyLinkedList([0, 1, 2, 3, 4])
PY
```

## Выводы по производительности

- Добавление и снятие элементов со «своего» края у стека и очереди выполняются за константное время.
- Очередь на `deque` выигрывает у реализации на списке при извлечении из начала из-за отсутствия сдвига элементов.
- Односвязный список обеспечивает быстрое добавление в начало/конец (при наличии `tail`), но требует линейного обхода для вставки в середину и поиска элементов.
