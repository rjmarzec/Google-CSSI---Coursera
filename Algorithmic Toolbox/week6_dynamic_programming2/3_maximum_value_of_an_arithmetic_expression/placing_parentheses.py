# Uses python3


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    values = []
    operations = []
    for i in range(len(dataset)):
        if i % 2 == 0:
            values.append(int(dataset[i]))
        else:
            operations.append(dataset[i])

    mins = [[0 for x in range(len(values))] for y in range(len(values))]
    maxes = [[0 for x in range(len(values))] for y in range(len(values))]
    for i in range(0, len(mins[0])):
        mins[i][i] = values[i]
        maxes[i][i] = values[i]

    for i in range(1, len(mins[0])):
        mins[i - 1][i] = evalt(mins[i - 1][i - 1], mins[i][i], operations[i-1])
        maxes[i - 1][i] = evalt(mins[i - 1][i - 1], mins[i][i], operations[i-1])

    for s in range(1, len(mins[0])):
        for i in range(0, len(mins[0]) - s):
            j = i + s
            mins[i][j], maxes[i][j] = min_and_max(i, j, mins, maxes, operations)

    return maxes[0][len(values) - 1]


def min_and_max(i, j, mins, maxes, operations):
    minimum = float('inf')
    maximum = float('-inf')
    for k in range(i, j):
        a = evalt(maxes[i][k], maxes[k + 1][j], operations[k])
        b = evalt(maxes[i][k], mins[k + 1][j], operations[k])
        c = evalt(mins[i][k], maxes[k + 1][j], operations[k])
        d = evalt(mins[i][k], mins[k + 1][j], operations[k])
        minimum = min(a, b, c, d, minimum)
        maximum = max(a, b, c, d, maximum)
    return minimum, maximum


def print_matrices(mins, maxes):
    print('\n')
    print('Mins:')
    for temp in mins:
        print(temp)
    print('Maxes:')
    for temp in maxes:
        print(temp)


if __name__ == "__main__":
    print(get_maximum_value(input()))
