# python3
global swaps


def build_heap(data):
    heap = data
    for i in range(len(data)-1, -1, -1):
        heap = sift_down(i, heap)
    return heap


def sift_down(i, heap):
    size = len(heap) - 1
    max_index = i

    l = left_child(i)
    if l <= size and heap[l] < heap[max_index]:
        max_index = l

    r = right_child(i)
    if r <= size and heap[r] < heap[max_index]:
        max_index = r

    if i != max_index:
        global swaps
        swaps.append(str(i-1) + ' ' + str(max_index-1))
        heap[i], heap[max_index] = heap[max_index], heap[i]
        sift_down(max_index, heap)

    return heap


def parent(i):
    return int(i/2)


def left_child(i):
    return i*2


def right_child(i):
    return i*2 + 1


def main():
    global swaps
    swaps = []
    n = int(input())
    data = list(map(int, input().split()))
    data.insert(0, 0)
    assert len(data) == n + 1

    result_heap = build_heap(data)
    num_of_swaps = len(swaps)

    print(num_of_swaps)
    if num_of_swaps > 0:
        for swap in swaps:
            print(swap)


if __name__ == "__main__":
    main()
