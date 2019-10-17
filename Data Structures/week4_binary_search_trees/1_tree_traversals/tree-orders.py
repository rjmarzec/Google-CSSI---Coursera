# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.in_order = []
        self.pre_order = []
        self.post_order = []
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def allOrders(self, current_key_index):
        self.pre_order.append(self.key[current_key_index])
        if self.left[current_key_index] != -1:
            self.allOrders(self.left[current_key_index])
        self.in_order.append(self.key[current_key_index])
        if self.right[current_key_index] != -1:
            self.allOrders(self.right[current_key_index])
        self.post_order.append(self.key[current_key_index])
        return

    def inOrder(self, current_key_index):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        # Order: Left - Middle - Right
        if self.left[current_key_index] != -1:
            result.extend(self.inOrder(self.left[current_key_index]))
        result.append(self.key[current_key_index])
        if self.right[current_key_index] != -1:
            result.extend(self.inOrder(self.right[current_key_index]))
        return result

    def preOrder(self, current_key_index):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        # Order: Middle - Left - Right
        result.append(self.key[current_key_index])
        if self.left[current_key_index] != -1:
            result.extend(self.preOrder(self.left[current_key_index]))
        if self.right[current_key_index] != -1:
            result.extend(self.preOrder(self.right[current_key_index]))
        return result

    def postOrder(self, current_key_index):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        # Order: Left - Right - Middle
        if self.left[current_key_index] != -1:
            result.extend(self.postOrder(self.left[current_key_index]))
        if self.right[current_key_index] != -1:
            result.extend(self.postOrder(self.right[current_key_index]))
        result.append(self.key[current_key_index])
        return result


def main():
    tree = TreeOrders()
    tree.read()
    tree.allOrders(0)
    # print(" ".join(str(x) for x in tree.inOrder(0)))
    # print(" ".join(str(x) for x in tree.preOrder(0)))
    # print(" ".join(str(x) for x in tree.postOrder(0)))
    print(" ".join(str(x) for x in tree.in_order))
    print(" ".join(str(x) for x in tree.pre_order))
    print(" ".join(str(x) for x in tree.post_order))


threading.Thread(target=main).start()

"""
Sample Examples:

5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1

10
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1

"""
