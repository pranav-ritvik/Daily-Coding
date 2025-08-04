# cook your dish here
T = int(input())
for test_case in range(T):
    R, C = map(int, input().split())
    matrix = []
    for row_index in range(R):
        matrix.append(input().strip().lower())
    found = False

    for row in matrix:
        if 'spoon' in row:
            found = True
            break

    if not found:
        for col_index in range(C):
            col = ''.join(matrix[row_index][col_index] for row_index in range(R))
            if 'spoon' in col:
                found = True
                break

    if found:
        print("There is a spoon!")
    else:
        print("There is indeed no spoon!")
