def find_most_frequent_number(n, a):
  from collections import Counter

  # Подсчитываем количество вхождений каждого числа в массиве
  count = Counter(a)

  # Находим максимальную частоту
  max_frequency = max(count.values())

  # Находим все числа с максимальной частотой
  max_frequency_numbers = [num for num, freq in count.items() if freq == max_frequency]

  # Возвращаем наибольшее из чисел с максимальной частотой
  return max(max_frequency_numbers)

# Чтение данных
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

# Решение задачи
result = find_most_frequent_number(n, a)
print(result)