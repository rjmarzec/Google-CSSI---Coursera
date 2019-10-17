# Uses python3
def calc_fib(n):
    first_60_nums = [0, 1, 1]

    while len(first_60_nums) < 60:
        first_60_nums.append(first_60_nums[len(first_60_nums) - 1] + first_60_nums[len(first_60_nums) - 2])

    return first_60_nums[n % 60] % 10

n = int(input())
print(calc_fib(n))
