# Uses python3
import sys


def get_optimal_value(capacity, weights_input, values):
    value = 0.
    # avoid consuming inputs
    weights = weights_input
    current_capacity = capacity

    value_per_weight = []
    for i in range(len(values)):
        value_per_weight.append(values[i]/weights[i])

    # zips weights & values per weight to sort, and returns them as 2 lists
    value_per_weight, weights = zip(*sorted(zip(value_per_weight, weights)))

    current_object = len(weights) - 1
    while current_capacity > 0 and current_object >= 0:
        if weights[current_object] < current_capacity:
            value += value_per_weight[current_object]*weights[current_object]
            current_capacity -= weights[current_object]
        else:
            value += value_per_weight[current_object]*current_capacity
            current_capacity = 0
        current_object -= 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
