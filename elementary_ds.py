# elementary_ds.py
from __future__ import annotations
from typing import Any, Optional, List


# ---------- Arrays & Matrices ----------
class DynamicArray:
    """Minimal dynamic array wrapper using Python list to model O(1) amortized append/insert/delete."""
    def __init__(self, items: Optional[List[Any]] = None):
        self._a: List[Any] = list(items) if items else []

    def access(self, i: int) -> Any:
        return self._a[i]

    def insert(self, i: int, x: Any) -> None:
        self._a.insert(i, x)  # O(n) worst-case shift

    def delete(self, i: int) -> Any:
        return self._a.pop(i)  # O(n) worst-case shift

    def append(self, x: Any) -> None:
        self._a.append(x)  # amortized O(1)

    def __len__(self) -> int:
        return len(self._a)

    def __repr__(self) -> str:
        return repr(self._a)


class Matrix:
    """Simple row-major matrix with basic ops: access, set, row/col insert/delete."""
    def __init__(self, rows: int, cols: int, fill: Any = 0):
        self.r = rows
        self.c = cols
        self._m = [[fill for _ in range(cols)] for _ in range(rows)]

    def access(self, i: int, j: int) -> Any:
        return self._m[i][j]

    def set(self, i: int, j: int, val: Any) -> None:
        self._m[i][j] = val

    def insert_row(self, i: int, fill: Any = 0) -> None:
        self._m.insert(i, [fill for _ in range(self.c)])
        self.r += 1

    def delete_row(self, i: int) -> List[Any]:
        self.r -= 1
        return self._m.pop(i)

    def insert_col(self, j: int, fill: Any = 0) -> None:
        for row in self._m:
            row.insert(j, fill)
        self.c += 1

    def delete_col(self, j: int) -> List[Any]:
        col = []
        for row in self._m:
            col.append(row.pop(j))
        self.c -= 1
        return col

    def __repr__(self) -> str:
        return "\n".join(str(row) for row in self._m)


# ---------- Stack and Queue (array-based) ----------
class ArrayStack:
    def __init__(self, capacity: int = 10):
        self._a = [None] * capacity
        self._top = 0  # next free slot

    def push(self, x: Any) -> None:
        if self._top == len(self._a):
            self._a.extend([None] * len(self._a or [None]))  # grow
        self._a[self._top] = x
        self._top += 1

    def pop(self) -> Any:
        if self.empty():
            raise IndexError("underflow")
        self._top -= 1
        x = self._a[self._top]
        self._a[self._top] = None
        return x

    def empty(self) -> bool:
        return self._top == 0

    def __len__(self) -> int:
        return self._top


class CircularArrayQueue:
    def __init__(self, capacity: int = 8):
        self._a = [None] * (capacity + 1)  # one slot left empty
        self._head = 0
        self._tail = 0

    def enqueue(self, x: Any) -> None:
        nxt = (self._tail + 1) % len(self._a)
        if nxt == self._head:
            # grow
            self._grow()
            nxt = (self._tail + 1) % len(self._a)
        self._a[self._tail] = x
        self._tail = nxt

    def dequeue(self) -> Any:
        if self._head == self._tail:
            raise IndexError("underflow")
        x = self._a[self._head]
        self._a[self._head] = None
        self._head = (self._head + 1) % len(self._a)
        return x

    def _grow(self) -> None:
        old = self.to_list()
        newcap = 2 * (len(self._a) - 1)
        self._a = [None] * (newcap + 1)
        self._head = self._tail = 0
        for x in old:
            self.enqueue(x)

    def to_list(self) -> List[Any]:
        res = []
        i = self._head
        while i != self._tail:
            res.append(self._a[i])
            i = (i + 1) % len(self._a)
        return res

    def __len__(self) -> int:
        return len(self.to_list())


# ---------- Singly Linked List ----------
class SLLNode:
    __slots__ = ("key", "next")
    def __init__(self, key: Any):
        self.key = key
        self.next: Optional["SLLNode"] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[SLLNode] = None

    def insert_front(self, x: Any) -> None:
        node = SLLNode(x)
        node.next = self.head
        self.head = node

    def search(self, k: Any) -> Optional[SLLNode]:
        cur = self.head
        while cur and cur.key != k:
            cur = cur.next
        return cur

    def delete(self, k: Any) -> bool:
        prev = None
        cur = self.head
        while cur and cur.key != k:
            prev, cur = cur, cur.next
        if not cur:
            return False
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
        return True

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.key
            cur = cur.next

    def __repr__(self) -> str:
        return "->".join(str(x) for x in self)

if __name__ == "__main__":
    print("=== Testing DynamicArray ===")
    arr = DynamicArray([1, 2, 3])
    arr.append(4)
    arr.insert(2, 99)
    print("After insert:", arr)
    arr.delete(1)
    print("After delete:", arr)

    print("\n=== Testing Matrix ===")
    m = Matrix(2, 3, fill=0)
    m.set(0, 1, 5)
    m.insert_row(1, fill=9)
    print("Matrix:\n", m)

    print("\n=== Testing ArrayStack ===")
    s = ArrayStack()
    s.push(10); s.push(20); s.push(30)
    print("Popped:", s.pop())
    print("Stack length:", len(s))

    print("\n=== Testing CircularArrayQueue ===")
    q = CircularArrayQueue(3)
    for i in range(5):
        q.enqueue(i)
    print("Dequeued:", q.dequeue())
    print("Queue contents:", q.to_list())

    print("\n=== Testing SinglyLinkedList ===")
    ll = SinglyLinkedList()
    ll.insert_front(10)
    ll.insert_front(20)
    ll.insert_front(30)
    print("List after inserts:", ll)
    ll.delete(20)
    print("List after delete:", ll)

