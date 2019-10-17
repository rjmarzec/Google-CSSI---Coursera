# python3
import sys

'''
2

'''

def optimal_summands(n):
    summands = []
    remaining_n = n
    current_num = 1

    while current_num <= remaining_n:
        summands.append(current_num)
        remaining_n -= current_num
        current_num += 1

    summands[len(summands) - 1] += remaining_n

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
