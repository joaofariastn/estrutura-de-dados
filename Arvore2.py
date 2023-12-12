class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


data = [200, 450, 123, 52, 133, 321, 422, 523, 36, 64]

root = None
for num in data:
    root = insert(root, num)



print("Árvore Binária em Ordem:")
inorder_traversal(root)

def depth_of_tree(root):
    if root is None:
        return 0
    else:
        left_depth = depth_of_tree(root.left)
        right_depth = depth_of_tree(root.right)
        return max(left_depth, right_depth) + 1

profundidade = depth_of_tree(root) -1
print("\nProfundidade da árvore:", profundidade)

def encontrar_nos_folhas(root):
    folhas = []

    def inorder_para_folhas(node):
        if node:
            inorder_para_folhas(node.left)
            if node.left is None and node.right is None:
                folhas.append(node.val)
            inorder_para_folhas(node.right)

    inorder_para_folhas(root)
    return folhas


nos_folhas = encontrar_nos_folhas(root)
print("Nós Folhas:", nos_folhas)
