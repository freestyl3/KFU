import math
from pprint import pprint

epsilon = 10 ** (-6)
a = 0
b = 4
n = 10
h = round((b - a) / n, 2)
x_values = [round(a + i * h, 2) for i in range(n + 1)]

def main():
    function_values = {x: round(calculate(x), 6) for x in x_values}
    print_values(function_values)


def calculate(x, accuracy=epsilon):
    result = 0
    n = 0
    while True:
        term = ( ((-1) ** n * x ** (2 * n + 1)) /
                ((2 * n + 1) * (math.factorial((2 * n + 1)))) )
        result += term
        if abs(term) < accuracy:
            break
        n += 1
    return result

def print_values(values: dict):
    for key, value in values.items():
        print(key, value)


if __name__ == '__main__':
    main()