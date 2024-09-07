def factorial(n):
    # Проверяем, является ли число отрицательным, нулем или положительным
    if n < 0:
        return "Факториал не определен для отрицательных чисел"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Запрашиваем у пользователя ввод числа
try:
    number = int(input("Введите число: "))
    print(f"Факториал числа {number} равен {factorial(number)}")
except ValueError:
    print("Пожалуйста, введите целое число.")