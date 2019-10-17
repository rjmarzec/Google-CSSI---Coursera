# Uses python3
def calc_fib(n):
    fib_counter_counter = 1
    num1 = 0
    num2 = 1

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        while fib_counter_counter < n:
            temp_num = num1 + num2
            num1 = num2
            num2 = temp_num
            fib_counter_counter += 1
        return num2

n = int(input())
print(calc_fib(n))
