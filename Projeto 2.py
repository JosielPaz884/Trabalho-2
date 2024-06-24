import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node is not None:
            print(f"Valor do nó: {node.value}")
            print(f"Filho esquerdo: {node.left.value if node.left else 'None'}")
            print(f"Filho direito: {node.right.value if node.right else 'None'}")
            print()
            self._print_tree_recursive(node.left)
            self._print_tree_recursive(node.right)

class PriorityQueue:
    def __init__(self, type):
        self.heap = []
        self.type = type

    def insert(self, value):
        if self.type == "min":
            heapq.heappush(self.heap, value)
        elif self.type == "max":
            heapq.heappush(self.heap, -value)
        elif self.type == "fibonacci":
            self.heap.append(value)
            self._heapify_fibonacci(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) == 0:
            return None
        if self.type == "min":
            return heapq.heappop(self.heap)
        elif self.type == "max":
            return -heapq.heappop(self.heap)
        elif self.type == "fibonacci":
            if len(self.heap) == 0:
                return None
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  
            min_value = self.heap.pop()  
            self._heapify_fibonacci(0)
            return min_value

    def _heapify_fibonacci(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest!= i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_fibonacci(smallest)

    def is_empty(self):
        return len(self.heap) == 0

tree = BinaryTree()
pq_min = PriorityQueue("min")
pq_max = PriorityQueue("max")
pq_fib = PriorityQueue("fibonacci")

values = [5, 3, 7, 2, 4, 6, 8]
for value in values:
    tree.insert(value)
    pq_min.insert(value)
    pq_max.insert(value)
    pq_fib.insert(value)

print("Árvore original:")
tree.print_tree()

print("Fila de prioridade mínima:")
while not pq_min.is_empty():
    value = pq_min.extract()
    print(value)

print("Fila de prioridade máxima:")
while not pq_max.is_empty():
    value = pq_max.extract()
    print(value)

print("Fila de prioridade Fibonacci:")
while not pq_fib.is_empty():
    value = pq_fib.extract()
    print(value)
