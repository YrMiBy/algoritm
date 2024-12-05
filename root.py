# Дерево
class Node():
    def __init__(self, key):
        self.left = None  # левая ветка
        self.right = None  # правя ветка
        self.val = key  # значение

        # Функция для добавления нового узла
        def insert(root, key):  # root - узел, key - значение узла
            if root is None:  # Если корневого узла нет, он создается (Node)
                return Node(key)
            else:
                if key < root.val:  # Если новое значение меньше текущего, добавляется в левое поддерево
                    root.left = insert(root.left, key)
                else:  # Иначе в правое поддерево
                    root.right = insert(root.right, key)
            return root  # возвращаем текущий корень дерева

        root = Node(90)
        root = insert(root, 55)
        root = insert(root, 99)
        root = insert(root, 56)
        root = insert(root, 45)
        root = insert(root, 60)
        root = insert(root, 73)
        root = insert(root, 100)

