import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Вузол дерева


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())

# Додати ребра для вузлів дерева


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

# Функція для візуалізації дерева


def draw_tree(tree_root, step):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.title(f'Крок {step}')
    plt.show()

# Функція для генерування кольорів


def generate_color(step, max_steps):
    intensity = int(255 * (step / max_steps))
    hex_color = f'#{intensity:02X}{(255 - intensity):02X}{128:02X}'
    return hex_color

# Обхід у глибину (DFS) з використанням стека


def dfs(tree_root):
    stack = [tree_root]
    step = 0
    max_steps = 0
    current = tree_root
    nodes = [tree_root]
    while stack:
        node = stack.pop()
        step += 1
        node.color = generate_color(step, len(nodes))
        draw_tree(tree_root, step)

        # Додаємо дітей у стек (спочатку правий, потім лівий)
        if node.right:
            stack.append(node.right)
            nodes.append(node.right)
        if node.left:
            stack.append(node.left)
            nodes.append(node.left)

# Обхід у ширину (BFS) з використанням черги


def bfs(tree_root):
    queue = deque([tree_root])
    step = 0
    max_steps = 0
    nodes = [tree_root]
    while queue:
        node = queue.popleft()
        step += 1
        node.color = generate_color(step, len(nodes))
        draw_tree(tree_root, step)

        # Додаємо дітей у чергу (зліва направо)
        if node.left:
            queue.append(node.left)
            nodes.append(node.left)
        if node.right:
            queue.append(node.right)
            nodes.append(node.right)

# Створення дерева


def build_tree():
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)
    return root


# Вибір способу обходу та запуск програми
tree_root = build_tree()

print("Оберіть тип обходу: 1 - DFS (в глибину), 2 - BFS (в ширину)")
choice = int(input("Ваш вибір: "))

if choice == 1:
    print("Обхід у глибину (DFS):")
    dfs(tree_root)
elif choice == 2:
    print("Обхід у ширину (BFS):")
    bfs(tree_root)
else:
    print("Неправильний вибір.")
