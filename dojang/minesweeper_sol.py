col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(col):
    for j in range(row):
        if matrix[i][j] == "*":
            continue
        # 요소가 지뢰가 아닐 경우 0을 넣습니다.
        else:
            matrix[i][j] = 0


            # 요소의 주변 8칸을 탐색합니다.
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    # 탐색하는 칸이 2차원 리스트의 범위를 벗어나면 건너뜁니다.
                    if k < 0 or k >= row or l < 0 or l >= col:
                        continue
                    # 탐색하는 칸이 지뢰일 경우 요소에 1 더합니다.
                    if matrix[l][k] == "*":
                            matrix[i][j] += 1

for i in range(col):
    for j in range(row):
        print(matrix[i][j], end="")
    print()