# Стек
class Stack:  # класс стек
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]  # создание списка

    def is_empty(self):  # проверка пуст ли список
        return self.items == []

    def push(self, item):  # функция добавления элемента в список
        self.items.append(item)

    def pop(self):  # функция удаления верхнего элемента из списка
        return self.items.pop()

    def peek(self):  # функция получения верхнего элемента из списка без его удаления
        return self.items[-1]

stack = Stack()  # создание объекта класса стек

if stack.is_empty() == True:  # проверка стека на пустоту
    print('Стек пустой')
else: print(stack.peek())  # вывод последнего элемента

stack.push(6)
print(stack.peek())
stack.pop()
print(stack.peek())

