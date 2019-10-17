# Uses python3


def edit_distance(t, s):
    matrix = [[0 for x in range(len(s) + 1)] for y in range(len(t) + 1)]

    for i in range(0, len(s) + 1):
        matrix[0][i] = i
    for i in range(0, len(t) + 1):
        matrix[i][0] = i

    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            insertion = matrix[j - 1][i] + 1
            deletion = matrix[j][i - 1] + 1
            match = matrix[j - 1][i - 1]
            mismatch = matrix[j - 1][i - 1] + 1

            if list(s)[i - 1] == list(t)[j - 1]:
                matrix[j][i] = min(insertion, deletion, match)
            else:
                matrix[j][i] = min(insertion, deletion, mismatch)

    return matrix[len(t)][len(s)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
