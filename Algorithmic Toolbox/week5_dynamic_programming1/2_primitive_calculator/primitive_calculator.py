# Uses python3
import sys


def optimal_sequence(n):
    sequence = [None] * (n + 1)
    sequence[n] = 0
    sequence[0] = 0
    for i in reversed(range(1, n)):
        # Organized as [*3, *2, +1]
        steps_from_moves = [None, None, None]
        if i * 3 <= n:
            steps_from_moves[0] = sequence[i * 3] + 1
        if i * 2 <= n:
            steps_from_moves[1] = sequence[i * 2] + 1
        steps_from_moves[2] = sequence[i + 1] + 1
        sequence[i] = min(x for x in steps_from_moves if x is not None)

    result_sequence = [1]
    spot_counter = 1
    while len(result_sequence) - 1 != sequence[1]:
        # while result_sequence[len(result_sequence) - 1] > 0:
        if spot_counter * 3 <= n and sequence[spot_counter] == sequence[spot_counter * 3] + 1:
            spot_counter *= 3
            result_sequence.append(spot_counter)
        elif spot_counter * 2 <= n and sequence[spot_counter] == sequence[spot_counter * 2] + 1:
            spot_counter *= 2
            result_sequence.append(spot_counter)
        elif sequence[spot_counter] == sequence[spot_counter + 1] + 1:
            spot_counter += 1
            result_sequence.append(spot_counter)

    return result_sequence


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
