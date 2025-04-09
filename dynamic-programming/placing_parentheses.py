def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    numbers= dataset[::2]
    operators= dataset[1::2]
    n = len(numbers)
    max_sol= []
    min_sol= []
    for i in range(n):
        row = [0] * n
        row[i] = int(numbers[i])
        max_sol.append(row[:])
        min_sol.append(row[:])
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            max_sol[i][j]= float('-inf')
            min_sol[i][j]= float('inf')
            for k in range(i, j):
                a = evaluate(max_sol[i][k], max_sol[k + 1][j], operators[k])
                b = evaluate(min_sol[i][k], min_sol[k + 1][j], operators[k])
                c = evaluate(max_sol[i][k], min_sol[k + 1][j], operators[k])
                d = evaluate(min_sol[i][k], max_sol[k + 1][j], operators[k])
                max_sol[i][j] = max(max_sol[i][j], a, b, c, d)
                min_sol[i][j] = min(min_sol[i][j], a, b, c, d)
    print(max_sol)
    return max_sol[0][-1]


if __name__ == "__main__":
    print(maximum_value(input()))
