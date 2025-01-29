from math import sin, sqrt
from practice1 import calculate


A = 0
B = 4
H = 0.4

def left_rectangles(left, right):
    return (right - left) * function(left)


def trapezoid(left, right):
    c1 = (right - left) / 2
    return c1 * (function(left) + function(right))


def simpson(left, right):
    x1 = left
    x2 = (left + right) / 2
    x3 = right
    return (right - left) / 6 * (function(x1) + 4 * function(x2) + function(x3))


def gauss(left, right):
    x1 = (left + right) / 2 + (right - left) / 2 * (-sqrt(0.6))
    x2 = (left + right) / 2
    x3 = (left + right) / 2 + (right - left) / 2 * (sqrt(0.6))
    return (right - left) / 18 * (5 * function(x1) + 8 * function(x2) + 5 * function(x3))


def sum_of_functions(x_values, func):
    return sum([func(x_values[i], x_values[i + 1]) for i in range(len(x_values) - 1)])


def function(value):
    try:
        f = round(sin(value) / value, 6)
    except ZeroDivisionError:
        f = 1
    return f

def simple_form(x, x_values):
    left_limit = x_values[0]
    value = left_rectangles(left_limit, x)
    value = trapezoid(left_limit, x)
    value = simpson(left_limit,x)
    value = gauss(left_limit, x)
    print(f'Интеграл от {left_limit} до {x} = {value:.4f}')


def main():
    FUNCTIONS = (left_rectangles, trapezoid, simpson, gauss)
    x_values = [round(A + i * H, 2) for i in range(11)]

    for function in FUNCTIONS:
        print(f'{function.__name__: ^46}')
        print(f' Xn | {'Ряд': ^8} | {'Sn': ^8} | Погрешность | {'N': ^8}')
        for x in x_values:
            # simple_form(x, x_values)
            true_value = calculate(x)
            error = 1
            i = 1
            n = 2
            while error > 10 ** (-6) and n < 2 ** 10:
                n = 2 ** i
                h = (x - A) / n
                x_integrate_values = [A + j * h for j in range(n + 1)]
                value = sum_of_functions(x_integrate_values, function)
                error = abs(true_value - value)
                i += 1
            print(f'{x} | {true_value:.6f} | {value:.6f} | {error:.9f} | {n: >4}')
        print()

if __name__ == '__main__':
    main()