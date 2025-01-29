from math import cos, pi
from practice1 import calculate

import matplotlib.pyplot as plt


def Lagrange_polinome(x_values, y_values, xi):
    result = 0
    n = len(x_values)
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= ((xi - x_values[j]) / (x_values[i] - x_values[j]))
        result += term
    return result


def main():
    # print('Таблица значений функции Si(x)\n')
    # print('Zi  : Ln(Zi)  : Si(Zi)  : |Ln(Zi) - Si(Zi)|')
    a = 0
    b = 4
    n_list_t = []
    max_errors_list = []
    max_errors_list_t = []

    zi_list = []
    errors_list = []
    n = 5
    m = 10
    h1 = (b - a) / m

    # h = (b - a) / n



    for n in range(6, 31):
        h = (b - a) / n
        max_error = 0.0
        max_error_t = 0.0
        n_list_t.append(n)

        x_nodes = [round(a + i * h, 2) for i in range(n + 1)]
        x_nodes_t = [
            round((a + b) / 2, 2) +
            round((b - a) / 2, 2) *
            cos(round(((2 * i + 1) * pi) / (2 * n + 2), 2))
            for i in range(n + 1)
        ]
        y_nodes = [calculate(x) for x in x_nodes]
        y_nodes_t = [calculate(x) for x in x_nodes_t]

        for i in range(m + 1):
            zi = round(a + i * h1, 2)
            zi_list.append(zi)

            siZi = calculate(zi)
            lnZi = Lagrange_polinome(x_nodes, y_nodes, zi)
            error = abs(lnZi - siZi)

            max_error = max(error, max_error)

            lnZit = Lagrange_polinome(x_nodes_t, y_nodes_t, zi)
            error_t = abs(lnZit - siZi)
            max_error_t = max(error_t, max_error_t)
            errors_list.append(error_t)

            # print(f'{zi} : {lnZit:.6f} : {siZi:.6f} : {error_t:.6f}')

        print(f'{n} {max_error_t:.10f}')

        # fig, ax = plt.subplots()
        # ax.plot(zi_list, errors_list)
        # plt.show()

        max_errors_list.append(max_error)
        max_errors_list_t.append(max_error_t)

    fig, ax = plt.subplots()
    ax.plot(n_list_t, max_errors_list)
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(n_list_t, max_errors_list_t)
    plt.show()


if __name__ == '__main__':
    main()
