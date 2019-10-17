# python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []

    while len(segments) > 0:
        segments_to_remove = []
        lowest_max = segments[0].end
        lowest_segment = segments[0]

        # Find the lowest max
        for s in segments:
            if s.end < lowest_max:
                lowest_max = s.end
                lowest_segment = s
        segments.pop(segments.index(lowest_segment))

        for s in segments:
            if s.start <= lowest_max:
                segments_to_remove.append(s)

        points.append(lowest_max)
        for s in segments_to_remove:
            segments.pop(segments.index(s))

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
