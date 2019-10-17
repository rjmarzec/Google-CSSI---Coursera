# Uses python3

def get_change(m):
    remaining_change = m
    coins = [0, 0, 0]

    # 10's
    coins[0] = int(remaining_change/10)
    remaining_change -= coins[0] * 10

    # 5's
    coins[1] = int(remaining_change/5)
    remaining_change -= coins[1] * 5

    # 1's
    coins[2] = remaining_change

    # return the sum of all the coins
    return coins[0] + coins[1] + coins[2]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
