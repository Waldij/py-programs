"""
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц,
за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)
print(task("111111111111111111111111100000000"))
# >> OUT: 25...
"""


def task(array: str) -> int:
    return array.find('0')


def main():
    """
    Встроенный метод str.find вызывает Objects/stringlib/fastsearch.h
    n - длина строки
    m - длина подсторки
    В худшем случаем сложность будет O(n * m)
    Внекоторых случаях O(n / m)

    В нашей задаче, длина подсторки m = len('0') = 1
    И сложность будет O(n)
    """
    print(task("111111111111111111111111100000000"))


if __name__ == '__main__':
    main()