# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    min_refills = -1
    current_distance = 0

    while current_distance < distance:
        stop_possible = False
        current_farthest_stop = -1

        '1 2 5 9'
        for stop in stops:
            if stop - current_distance <= tank:
                stops = stops[stops.index(stop) + 1:]
                stop_possible = True
                current_farthest_stop = stop
            else:
                break

        if stop_possible:
            min_refills += 1
            current_distance = current_farthest_stop
        else:
            return -1
    return min_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
