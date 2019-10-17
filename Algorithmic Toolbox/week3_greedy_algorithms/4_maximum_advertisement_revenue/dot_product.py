# python3
import sys


def max_dot_product(a, b):
    res = 0

    while len(a) > 0:
        max_a = a[0]
        max_b = b[0]

        for num in a:
            if num > max_a:
                max_a = num
        for num in b:
            if num > max_b:
                max_b = num
        a.remove(max_a)
        b.remove(max_b)
        res += max_a*max_b

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

'''
1
23
39
'''

'''
3
1 3 -5
-2 4 1
'''
