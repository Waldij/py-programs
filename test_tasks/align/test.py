def who_is_next(n):
    """Решение в лоб"""
    # Напишите ваш код здесь
    starting_queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
    queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

    counter = 2

    for i in range(0, n):
        if len(queue) >= n:
            break
        for j in range(0, counter):
            queue.append(starting_queue[0])
        for j in range(0, counter):
            queue.append(starting_queue[1])
        for j in range(0, counter):
            queue.append(starting_queue[2])
        for j in range(0, counter):
            queue.append(starting_queue[3])
        for j in range(0, counter):
            queue.append(starting_queue[4])
        counter *= 2
    return queue[n - 1]


def who_is_next_2(n):
    """Более оптимальное решение"""
    # Напишите ваш код здесь
    starting_queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

    if n <= 5:
        return starting_queue[n - 1]

    # Вычиляем слой
    layer = layer_by_n(n, starting_queue)

    # Начальный индекс слоя
    layer_start_index = start_index_by_layer(layer, starting_queue)

    # Конечный индекс слоя
    layer_end_index = layer_start_index + (len(starting_queue) * (2 ** layer)) - 1

    k = (n - layer_start_index) / (layer_end_index - layer_start_index)
    index = index_by_k(k)

    return starting_queue[index]


def start_index_by_layer(layer, starting_queue):
    """Возвращает начальный индекс слоя"""
    layer_start_index = 1
    for i in range(1, layer + 1):
        layer_start_index += len(starting_queue) * (2 ** (i - 1))
    return layer_start_index


def layer_by_n(n, starting_queue):
    """Возвращает номер слоя по n"""
    layer = 1
    summ = 5
    while True:
        summ += len(starting_queue) * (2 ** layer)
        if summ >= n:
            break
        layer += 1
    return layer


def index_by_k(k):
    """Преобразует значение [0,1] в челое число от 0 до 4"""
    if k >= 0.8:
        return 4
    if k >= 0.6:
        return 3
    if k >= 0.4:
        return 2
    if k >= 0.2:
        return 1
    return 0


if __name__ == '__main__':
    for i in range(1, 1000):
        assert who_is_next(i) == who_is_next_2(i), 'Решения расходятся на {}'.format(i)
    print(who_is_next_2(1000000000000000000000000000))
