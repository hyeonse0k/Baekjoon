m , n = map(int, input().split())
castle = list()
for _ in range(m):
    castle.append(list(input().split()))

chk_column = 0
chk_row = 0

for i in range(m):
    need = False
    for j in range(n):
        if castle[i][j] == 'X':
            need = True
    if not need:
        chk_column += 1

for i in range(n):
    need = False
    for j in range(m):
        if castle[i][j] == 'X':
            need = True
    if not need:
        chk_row += 1

print(max(chk_row,chk_column))