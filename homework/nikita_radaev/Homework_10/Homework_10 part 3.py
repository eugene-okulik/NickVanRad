def decorate(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            op = '*'
        elif first == second:
            op = '+'
        elif first > second:
            op = '-'
        elif second > first:
            op = '/'
        else:
            op = '+'
        return func(first, second, op)

    return wrapper


@decorate
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            return "Ошибка: деление на ноль"
        return first / second
    else:
        return "Неизвестная операция"


try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = calc(a, b)
    print("Результат:", result)
except ValueError:
    print("Ошибка: введите корректные числа.")
