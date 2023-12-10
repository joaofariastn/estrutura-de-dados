class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ArvorBinaria:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type="in"):
        if traversal_type == "pre":
            return self.preorder_print(self.root, "")
        elif traversal_type == "in":
            return self.inorder_print(self.root, "")
        elif traversal_type == "post":
            return self.postorder_print(self.root, "")

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal

tree = ArvorBinaria(200)
tree.root.left = Node(450)
tree.root.right = Node(123)
tree.root.left.left = Node(52)
tree.root.left.right = Node(133)
tree.root.right.left = Node(321)
tree.root.right.right = Node(422)
tree.root.left.left.left = Node(523)
tree.root.left.left.right = Node(36)
tree.root.left.left.right.left = Node(64)
print("Árvore Binária: ")
print(tree.print_tree("pre")) # Pré-ordem
print(tree.print_tree("in"))   # Ordem Simétrica
print(tree.print_tree("post")) # Pós-ordem


print("\n \033[1;32;40m A profundidade da árvore formada é 5. Os nós que são nós folhas são os nós com os valores 64, 321 e 422. ")
