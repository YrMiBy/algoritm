#Очередь
class Queue:  # класс очередь
    def __init__(self):
       self.items = [5, 4, 3, 2, 1]

    def is_empty(self):  # проверка пуста ли очередь
       return self.items == []

    def enqueue(self, item):  # добавление элемента в конец очереди (в начало списка)
       self.items.insert(0, item)

    def dequeue(self): # удаление последнего элемента списка (из начала очереди)
       return self.items.pop()

    def size(self):  # метод для возвращения размера очереди
        return len(self.items)

queue = Queue()  # создание объекта класса очередь

if queue.is_empty() == True:  # проверка очереди на пустоту
    print('Очередь пуста')
else:
    print(f'Размер очереди: {queue.size()}')  # размер списка

print(f'Ушел из очереди: {queue.dequeue()}')
print(f'Размер очереди: {queue.size()}')  # размер списка


