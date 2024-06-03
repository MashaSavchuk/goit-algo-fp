"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
- написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

class LinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def __str__(self):
            return str(self.date)

    def __init__(self):
        self.head = None

    def add_first(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def delete_last(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        current_node = self.head
        previous_node = current_node
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def insert_by_index(self, value, index):
        if index == 0:
            self.add_first(value)
            return
        new_node = self.Node(value)
        node_number = 1
        current_node = self.head
        while current_node is not None:
            if index == node_number:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            node_number += 1

    def delete_by_index(self, index):
        if index == 0:
            self.delete_first()
            return
        node_number = 0
        current_node = self.head
        previous_node = current_node
        while current_node is not None:
            if index == node_number:
                previous_node.next = current_node.next
                current_node.next = None
                return
            previous_node = current_node
            current_node = current_node.next
            node_number += 1

    def set_value_by_index(self, value, index):
        node_number = 0
        current_node = self.head
        while current_node is not None:
            if node_number == index:
                current_node.data = value
                return
            current_node = current_node.next
            node_number += 1

    def get_value_by_index(self, index):
        node_number = 0
        current_node = self.head
        while current_node is not None:
            if index == node_number:
                return current_node.data
            current_node = current_node.next
            node_number += 1
        return None

    def get_length(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def reverse_list(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def sort(self):  # insertion sort method
        if self.head is None or self.head.next is None:
            return

        sorted_tail = self.head
        while sorted_tail.next:
            current = sorted_tail.next
            if current.data < self.head.data:
                # Move node to the beginning
                sorted_tail.next = current.next
                current.next = self.head
                self.head = current
            else:
                # Search for the correct spot in the sorted part
                search = self.head
                while search.next is not current and current.data > search.next.data:
                    search = search.next
                if search.next is not current:
                    sorted_tail.next = current.next
                    current.next = search.next
                    search.next = current
                else:
                    sorted_tail = sorted_tail.next

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data) + " -> "
            current_node = current_node.next
        else:
            result += "None"
        return result


def merge_lists(linked_list1, linked_list2):
    merged_list = LinkedList()

    current1 = linked_list1.head
    current2 = linked_list2.head

    while current1 and current2:
        if current1.data < current2.data:
            merged_list.add_last(current1.data)
            current1 = current1.next
        else:
            merged_list.add_last(current2.data)
            current2 = current2.next

    while current1:
        merged_list.add_last(current1.data)
        current1 = current1.next

    while current2:
        merged_list.add_last(current2.data)
        current2 = current2.next

    merged_list.sort()
    return merged_list


if __name__ == "__main__":
    # Test reverse_list method
    list_1 = LinkedList()

    list_1.add_first(5)
    list_1.add_first(7)
    list_1.add_last(2)
    print("Display list", list_1)
    list_1.reverse_list()
    print("Display list", list_1)
    print("List length", list_1.get_length())

    # Test sort method
    list_1.add_first(18)
    list_1.add_first(15)
    list_1.add_first(12)
    list_1.sort()
    print("Display list", list_1)

    # Test merge_lists function
    list_2 = LinkedList()
    list_1.add_first(105)
    list_1.add_first(79)
    list_1.add_last(202)

    merged_list = merge_lists(list_1, list_2)
    print("Merged list: ", merged_list)
