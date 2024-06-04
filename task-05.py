"""
Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, 
яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). 
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
"""

import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            lft = x - 1 / 2**layer
            pos[node.left.id] = (lft, y - 1)
            lft = add_edges(graph, node.left, pos, x=lft, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            rght = x + 1 / 2**layer
            pos[node.right.id] = (rght, y - 1)
            rght = add_edges(graph, node.right, pos, x=rght, y=y - 1, layer=layer + 1)
    return graph


def create_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    return tree, pos


def draw_tree(tree, pos, title=None):
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    if title:
        plt.title(title)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=1500, node_color=colors
    )
    plt.show()


def bfs(tree, node, visited=None, queue=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = [node]

    while queue:
        current_node = queue.pop(0)
        if current_node.id not in visited:
            visited.add(current_node.id)
            color_value = len(visited)
            tree.nodes[current_node.id]["color"] = colormap(
                color_value / len(tree.nodes)
            )

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        if queue:
            bfs(tree, queue[0], visited, queue)


def dfs(tree, node, visited=None, colormap=None):
    if visited is None:
        visited = set()
    if colormap is None:
        colormap = {}

    if node.id not in visited:
        visited.add(node.id)
        if node.id not in colormap:
            colormap[node.id] = generate_color(len(colormap), len(tree.nodes))

        tree.nodes[node.id]["color"] = colormap[node.id]

        if node.left:
            dfs(tree, node.left, visited, colormap)
        if node.right:
            dfs(tree, node.right, visited, colormap)


def generate_color(index, total_nodes):
    cmap = plt.get_cmap("plasma")
    return cmap(index / total_nodes)


if __name__ == "__main__":
    colormap = plt.get_cmap("plasma")
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    tree, pos = create_tree(root)
    draw_tree(tree, pos)

    bfs(tree, root)
    draw_tree(tree, pos, title="BFS in Binary Tree")

    dfs(tree, root)
    draw_tree(tree, pos, title="DFS in Binary Tree")
