# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right or left + 1 == right:
        return a[left]

    majority_left = get_majority_element(a, left, left + int((right-left)/2))
    majority_right = get_majority_element(a, left + int((right-left)/2), right)

    majority_count = int((right-left)/2) + 1
    left_count = 0
    right_count = 0

    for i in range(left, right):
        if a[i] == majority_left:
            left_count += 1
        if a[i] == majority_right:
            right_count += 1

    if left_count >= majority_count:
        return majority_left
    elif right_count >= majority_count:
        return majority_right
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
