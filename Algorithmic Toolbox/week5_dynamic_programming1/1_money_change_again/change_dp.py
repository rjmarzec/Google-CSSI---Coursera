# Uses python3
import sys


def get_change(m):
    coins_needed = [None] * (m + 1)
    if m < 4:
        if m == 0:
            return 0
        elif m == 1:
            return 1
        elif m == 2:
            return 2
        elif m == 3:
            return 1
        elif m == 4:
            return 1
    coins_needed[0] = 0
    coins_needed[1] = 1
    coins_needed[2] = 2
    coins_needed[3] = 1
    coins_needed[4] = 1
    for i in range(5, m + 1):
        one_more = coins_needed[i - 1] + 1
        three_more = coins_needed[i - 3] + 1
        four_more = coins_needed[i - 4] + 1
        if four_more <= three_more and four_more <= one_more:
            coins_needed[i] = four_more
        elif three_more <= four_more and three_more <= one_more:
            coins_needed[i] = three_more
        elif one_more <= four_more and one_more <= three_more:
            coins_needed[i] = one_more
        else:
            coins_needed[i] = 0
    return coins_needed[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
