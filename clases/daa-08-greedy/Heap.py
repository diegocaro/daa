# Heap implementation, can be work adapted to any type.

# Class Node for Heap
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.right = None
        self.left = None

# Class Heap. Meant to orden list of objects by an arbitrary rule (ascending)
class Heap:
    def __init__(self):
        self.root = [None]
        self.size = 1

    def _parent(self, i):
        return i//2

    def _left_child(self, i):
        return 2*i

    def _right_child(self, i):
        return 2*i + 1

    def _swap(self, src, dst):
        self.root[src], self.root[dst] = self.root[dst], self.root[src]

    def push(self, node):
        self.root.append(node)
        i = self.size
        self.size += 1
        while i > 0 and self._parent(i) > 0:
            if self.root[self._parent(i)].freq > self.root[i].freq:
                self._swap(i, self._parent(i))
                i = self._parent(i)
            else:
                break
    def pop(self):
        self._swap(1, self.size - 1)
        ret = self.root.pop()
        self.size -= 1
        i = 1
        while (i < self.size and self._left_child(i) < self.size and
               self._right_child(i) < self.size):
            if self.root[self._left_child(i)].freq < self.root[i].freq:
                self._swap(i, self._left_child(i))
                i = self._left_child(i)
            elif self.root[self._right_child(i)].freq < self.root[i].freq:
                self._swap(i, self._right_child(i))
                i = self._right_child(i)
            else:
                break
        return ret
