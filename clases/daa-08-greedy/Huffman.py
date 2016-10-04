class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.right = None
        self.left = None

class Heap:
    def __init__(self):
        self.root = [None]

    def _parent(self, i):
        return i//2

    def _left_child(self, i):
        return 2*i

    def _right_child(self, i):
        return 2*i + 1

    def push(self, Node):
        self.root.append(Node)
        pass
        #TODO: PUSH, POP Y HUFFMAN

    def pop(self):
        pass

def Huffman(input):
    pass
