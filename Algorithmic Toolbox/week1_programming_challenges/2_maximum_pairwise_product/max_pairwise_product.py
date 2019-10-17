# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    num1 = 0
    num2 = 0

    for first in range(n):
        if numbers[first] > num1 or numbers[first] > num2:
            if num1 > num2:
                num2 = numbers[first]
            else:
                num1 = numbers[first]

    max_product = num1 * num2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
