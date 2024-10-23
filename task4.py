import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer  # Відстань лівого дочірнього елемента
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer  # Відстань правого дочірнього елемента
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Функція для побудови дерева на основі бінарної купи
def build_heap_tree(heap):
    # Функція для створення дерева з масиву (бінарна купа)
    def build_node(heap, i, n):
        if i >= n:
            return None
        root = Node(heap[i])  # Створюємо вузол для поточного індексу
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        root.left = build_node(heap, left_child_index, n)
        root.right = build_node(heap, right_child_index, n)
        return root

    # Побудова дерева
    n = len(heap)
    return build_node(heap, 0, n)


# Масив, що представляє бінарну купу
heap = [0, 4, 1, 5, 10, 3]

# Побудова дерева з бінарної купи
heap_tree_root = build_heap_tree(heap)

# Відображення дерева
draw_tree(heap_tree_root)
