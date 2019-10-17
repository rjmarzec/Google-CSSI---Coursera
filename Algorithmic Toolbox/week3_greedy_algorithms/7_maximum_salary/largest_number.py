# python3
import sys


def largest_number(a):
    res = ""

    while len(a) > 0:
        next_largest_num = 0

        for num in a:
            if int(str(next_largest_num) + str(num)) < int(str(num) + str(next_largest_num)):
                next_largest_num = num
        res += str(next_largest_num)
        a.pop(a.index(next_largest_num))

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
