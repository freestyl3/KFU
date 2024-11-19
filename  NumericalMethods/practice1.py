import math
from pprint import pprint

epsilon = 10 ** (-6)
x_values = [0.8, 2.0, 3.2]

def main():
    function_values = {x: calculate(x) for x in x_values}
    pprint(function_values)


def calculate(x, accuracy=epsilon):
    result = 0
    term = x
    n = 0
    while abs(term) > accuracy:
        term = ( ((-1) ** n * x ** (2 * n + 1)) /
                ((2 * n + 1) * (math.factorial((2 * n + 1)))) )
        result += term
        n += 1
    return result


if __name__ == '__main__':
    main()