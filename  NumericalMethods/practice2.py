from practice1 import calculate

a = 0
b = 4
n = 5
m = 10
h1 = (a + b) / n
h2 = (a + b) / m

x_values_n = [round(a + i * h1, 1) for i in range(n + 1)]
x_values_m = [round(a + i * h2, 2) for i in range(m + 1)]


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
    # function_values_n = [calculate(x) for x in x_values_n]
    # lagrange_values_m = [Lagrange_polinome(x, x_values_m, m) for x in x_values_m]
    # print(function_values_n)
    # print(lagrange_values_m)
    y_values = [calculate(x) for x in x_values_m]
    for i in range(m + 1):
        x = x_values_m[i]
        Lagrange_value = Lagrange_polinome(x_values_m, y_values, x_values_m[i])
        function_value = calculate(x)
        print(x, Lagrange_value, function_value, Lagrange_value - function_value)


if __name__ == '__main__':
    main()