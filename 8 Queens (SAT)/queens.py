import sys

N = int(sys.argv[1])

size = N * N

clauses = []

# 1)
for i in range(1, N + 1):
    arr = []
    clauses.append(arr)
    for j in range(1, N + 1):
        arr.append((i - 1) * N + j)

# 2)
for i in range(1, N + 1):

    row_index = (i - 1) * N

    for j in range(1, N + 1):

        index = row_index + j

# row
        r_start = row_index + 1
        r_end = (N * i)

        for x in range(r_start, r_end + 1):
            if x != index:
                clauses.append([-index, -x])

# column
        c_start = j
        c_end = N * (N - 1) + j

        for y in range(c_start, c_end + 1, N):
            if y != index:
                clauses.append([-index, -y])

# diagonals
        # left - right
        d_1_up_index = index - N - 1
        coords = [i - 1, j - 1]

        while coords[0] > 0 and coords[1] > 0:
            clauses.append([-index, -d_1_up_index])
            d_1_up_index = d_1_up_index - N - 1
            coords[0] -= 1
            coords[1] -= 1

        d_1_down_index = index + N + 1
        coords = [i + 1, j + 1]

        while coords[0] < N + 1 and coords[1] < N + 1:
            clauses.append([-index, -d_1_down_index])
            d_1_down_index = d_1_down_index + N + 1
            coords[0] += 1
            coords[1] += 1

        # right - left
        d_2_up_index = index - N + 1
        coords = [i - 1, j + 1]

        while coords[0] > 0 and coords[1] < N + 1:
            clauses.append([-index, -d_2_up_index])
            d_2_up_index = d_2_up_index - N + 1
            coords[0] -= 1
            coords[1] += 1

        d_2_down_index = index + N - 1
        coords = [i + 1, j - 1]

        while coords[0] < N + 1 and coords[1] > 0:
            clauses.append([-index, -d_2_down_index])
            d_2_down_index = d_2_down_index + N - 1
            coords[0] += 1
            coords[1] -= 1

# c
print("c n_queens_problem")

# p
print("p cnf", size, len(clauses))

# clauses
for i in range(len(clauses)):
    print(' '.join(map(str, clauses[i])) + ' 0')
