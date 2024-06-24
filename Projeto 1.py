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
            print(f"Filho esquerdo: {node.left.value if node.left else None}")
            print(f"Filho direito: {node.right.value if node.right else None}")
            print()
            self._print_tree_recursive(node.left)
            self._print_tree_recursive(node.right)

    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_value = self._find_min(node.right)
                node.value = min_value
                node.right = self._remove_recursive(node.right, min_value)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.value


tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Árvore original:")
tree.print_tree()

tree.remove(4)

print("Árvore após remoção de 4:")
tree.print_tree()

tree.remove(7)

print("Árvore após remoção de 7:")
tree.print_tree()
