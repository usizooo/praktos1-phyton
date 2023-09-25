import math
import string


def proverka(x):
    if x in string.digits:
        return 'YES'
    else:
        return 'NO'


operator = input("Введите оператор (+, -, *, /, степень, квадратный корень, !, sin, cos, tan): ")

if operator == "+":
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    if proverka(a) != 'YES' or proverka(b) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = float(a) + float(b)

elif operator == "-":
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    if proverka(a) != 'YES' or proverka(b) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = float(a) - float(b)

elif operator == "*":
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    if proverka(a) != 'YES' or proverka(b) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = float (a) * float (b)

elif operator == "/":
    a = input("Введите первое число:")
    b = input("Введите второе число:")
    if proverka(a) != 'YES' or proverka(b) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    if b == '0':
        print("нельзя делить на ноль")
        exit()
    res = float (a) / float (b)

elif operator == "степень":
    a = input("Введите число:")
    b = input("Введите степень числа:")
    if proverka(a) != 'YES' or proverka(b) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = float(a) ** float(b)

elif operator == "квадратный корень":
    a = input("Введите число:")
    if proverka(a) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = math.sqrt(float(a))

elif operator == "!":
    a = input("Введите число:")
    if proverka(a) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = math.factorial(float(a))

elif operator == "sin":
    a = input("Введите радианы:")
    if proverka(a) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = math.sin(float(a))

elif operator == "cos":
    a = input("Введите радианы:")
    if proverka(a) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = math.cos(float(a))

elif operator == "tan":
    a = input("Введите радианы:")
    if proverka(a) != 'YES':
        print("Ошибка: введены некорректные данные")
        exit()
    res = math.tan(float(a))

else:
    print("Ошибка: введены некорректные данные")
    exit()

print("Результат:", res)
