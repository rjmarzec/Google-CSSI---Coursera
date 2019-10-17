#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size

global in_order_list
global is_binary


def in_order_traversal(tree, current_key_index):
    global in_order_list
    global is_binary
    left_child_index = tree[current_key_index][1]
    right_child_index = tree[current_key_index][2]

    # Order: Left - Middle - Right
    if left_child_index != -1:
        if tree[current_key_index][0] == tree[left_child_index][0]:
            is_binary = False
        in_order_traversal(tree, left_child_index)
    in_order_list.append(tree[current_key_index][0])
    if right_child_index != -1:
        in_order_traversal(tree, right_child_index)
    return


def main():
    global in_order_list
    global is_binary
    in_order_list = []
    is_binary = True

    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    # tree[x][0] = key
    # tree[x][1] = left child index (if != -1)
    # tree[x][2] = right child index (if != -1)

    if len(tree) > 0:
        in_order_traversal(tree, 0)
        for i in range(0, len(in_order_list) - 1):
            if in_order_list[i] > in_order_list[i + 1]:
                is_binary = False

    if is_binary:
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

"""
Sample Examples:

3
2 1 2
1 -1 -1
3 -1 -1

3
1 1 2
2 -1 -1
3 -1 -1

0

5
1 -1 1
2 -1 2
3 -1 3
4 -1 4
5 -1 -1

4
4 1 -1
2 2 3
1 -1 -1
5 -1 -1

3
2 1 2
2 -1 -1
3 -1 -1

"""
