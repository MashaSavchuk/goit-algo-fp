"""
Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
"""

import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="lightgreen"):
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
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def draw_heap(heap_list):
    heap_root = Node(heap_list[0])
    nodes = [heap_root]

    for i in range(len(heap_list)):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        if left_child_idx < len(heap_list):
            nodes[i].left = Node(heap_list[left_child_idx])
            nodes.append(nodes[i].left)
        if right_child_idx < len(heap_list):
            nodes[i].right = Node(heap_list[right_child_idx])
            nodes.append(nodes[i].right)

    heap_graph = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap_graph = add_edges(heap_graph, heap_root, pos)

    colors = [node[1]["color"] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 6))
    plt.title("Heap visualisation")
    nx.draw(
        heap_graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=1500,
        node_color=colors,
    )
    plt.show()


if __name__ == "__main__":
    heap = [12, 75, 56, 98, 87, 42, 61, 59, 0, 92]
    heapq.heapify(heap)
    draw_heap(heap)
    