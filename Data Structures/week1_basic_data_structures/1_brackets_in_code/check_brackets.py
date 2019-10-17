# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    counter_stack = []
    index_counter = 0
    for i, next in enumerate(text):
        index_counter += 1
        if next in "([{":
            opening_brackets_stack.append(next)
            counter_stack.append(index_counter)
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return index_counter
            elif not are_matching(opening_brackets_stack.pop(), next):
                return index_counter
            counter_stack.pop()
            pass
    if not opening_brackets_stack:
        return 'Success'
    return counter_stack.pop()


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
