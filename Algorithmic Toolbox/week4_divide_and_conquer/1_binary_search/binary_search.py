# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)-1
    while True:
        middle = left + int((right-left)/2)
        if a[middle] == x:
            return middle
        elif right-left == 0:
            return -1
        elif x > a[middle]:
            left = middle+1
        else:
            right = middle


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
