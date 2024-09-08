import numpy as np

def score_game(game_core_v3) -> int:
    """Функция для оценки, за какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # Создаем пустой список для сохраенния туда числа попыток каждого подхода
    np.random.seed(1)  # Сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список из 1000 случайных чисел

    for number in random_array:
        count_ls.append(game_core_v3(number)) # Добавляем результат с количеством попыток в наш список

    score = int(np.mean(count_ls)) # вычисляем среднее значение количества попыток 1000 подходов
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    

def game_core_v3(number: int = 1) -> int:
    """Функция которая угадывает загаданное число, учитывая информацию больше или меньше случайное число нужного нам числа
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1, 101)
    
    min_zone = 1 # Определяем минимальный диапазон чисел для очередной попытки угадывания, на старте 1
    max_zone = 101 # Определяем минимальный диапазон чисел для очередной попытки угадывания, на старте 101
    
    while number != predict:
        count += 1
        
        if number > predict:
            min_zone = predict # корректируем меньшую границу диапазона
            predict = np.random.randint(min_zone, max_zone) # Берем случайное число в актуальном диапазоне
        elif number < predict:
            max_zone = predict # корректируем большую границу диапазона
            predict = np.random.randint(min_zone, max_zone) # Берем случайное число в актуальном диапазоне
    return count
    # Ваш код заканчивается здесь

    return count


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

