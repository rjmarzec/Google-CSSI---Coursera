# Uses python3


def lcm(a, b):
    current_a_mult = a
    current_b_mult = b
    a_times_b = a*b

    while a_times_b > current_a_mult and a_times_b > current_b_mult:
        if current_a_mult == current_b_mult:
            return current_a_mult
        elif current_a_mult < current_b_mult:
            current_a_mult += a
        elif current_b_mult < current_a_mult:
            current_b_mult += b
    return a*b


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))
