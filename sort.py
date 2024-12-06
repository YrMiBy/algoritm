def quick_sort(s):
    if len(s) <= 1:  # проверка условия выхода (длина списка <= 1)
        return s

    element = s[1]  # опорный элемент (при значении > 1 дает ошибку)
    left = list(filter(lambda i: i < element, s))  # левая часть, фильтр выбирает элементы меньше опорного
    center = [i for i in s if i == element]  # центр, фильтр выбирает элементы равные опорному
    right = list(filter(lambda i: i > element, s))  # правая часть, фильтр выбирает элементы больше опорного

    return quick_sort(left) + center + quick_sort(right)  # возвращение значений

print(quick_sort([3, 8, 6, 12, 56, 400, 8, 1]))


