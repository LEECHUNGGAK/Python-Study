col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

extended_y = [[0 for i in range(col + 2)] for j in range(row + 2)]

mine_index = []

for i in range(col):
    for j in range(row):
        # 탐색하는 칸이 지뢰일 경우 인덱스를 저장하고 이웃하는 칸에 1 더합니다.
        if matrix[i][j] == "*":
            mine_index .append([i, j])

            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    extended_y[k, l] += 1

# 패딩을 제거합니다.
y = []
for i in range(1, 1 + row):
    y.append(extended_y[i][1:-1])

# 지뢰를 추가합니다.
for i, j in mine:
    y[i][j] = "*"

for i in range(col):
    for j in range(row):
        print(y[i][j], end="")
    print()