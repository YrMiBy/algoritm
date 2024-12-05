# Граф
class Graph:
    def __init__(self):
       self.graph = {}  # создаем словарь

    def add_edge(self, u, v):  # метод для добавления ребра от одного узла (u) к другому (v)
        if u not in self.graph:  # проверка существует ли узел u
            self.graph[u] = []  # Если нет, то создаём для него пустой список связей
        self.graph[u].append(v)  # добавляем узел v в список связей для узла u.

    # вывод всех узлов графа и узлов, с которыми они соединены
    def print_graph(self):
        # {0: [2, 3, 4], 1: [2,  4], 2: [4], 3: [1, 4]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()  # объект класса

g.add_edge(0, 2)  # связи узлов графа
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 1)
g.add_edge(3, 4)

g.print_graph()  # вывод результатов
