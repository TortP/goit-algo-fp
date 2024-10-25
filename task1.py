class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елемента в початок списку
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Виведення елементів списку
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Функція реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо наступний вузол
            current.next = prev       # Міняємо напрямок посилання
            prev = current            # Переходимо до наступного елементу
            current = next_node
        self.head = prev

    # Функція для злиття двох відсортованих списків
    def sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    # Функція для поділу списку на дві половини
    def split(self, head):
        if head is None or head.next is None:
            return head, None

        slow = head
        fast = head.next

        # Рухаємося по списку, щоб знайти середину
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        return head, mid

    # Основна функція для сортування злиттям
    def merge_sort(self, h):
        if h is None or h.next is None:
            return h

        left, right = self.split(h)
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.sorted_merge(left, right)

    # Функція для об'єднання двох відсортованих списків
    def merge_two_sorted_lists(self, list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next


# Створення двох списків і додавання елементів
list1 = LinkedList()
list1.push(3)
list1.push(5)
list1.push(1)

list2 = LinkedList()
list2.push(4)
list2.push(2)
list2.push(6)

# Сортування кожного списку
list1.head = list1.merge_sort(list1.head)
list2.head = list2.merge_sort(list2.head)

# Виведення початкових списків
print("Список 1:")
list1.print_list()

print("Список 2:")
list2.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList()
merged_list.head = merged_list.merge_two_sorted_lists(list1.head, list2.head)

# Виведення результату
print("Об'єднаний відсортований список:")
merged_list.print_list()
