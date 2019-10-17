# Uses python3
import sys


def optimal_weight(capacity, items):
    matrix = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for w in range(1, W + 1):
            matrix[i][w] = matrix[i-1][w]
            if items[i-1] <= w:
                val = matrix[i-1][w-items[i-1]] + items[i-1]
                if matrix[i][w] < val:
                    matrix[i][w] = val

    return matrix[len(items)][capacity]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
