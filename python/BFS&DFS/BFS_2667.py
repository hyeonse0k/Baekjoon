from _collections import deque
def bfs(x,y):
    global group_count
    count = 1
    q = deque()
    q.append((x,y))
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        v = q.popleft()
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            for dx, dy in direction:
                nx, ny = v[0] + dx, v[1] + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if arr[nx][ny] and not visited[nx][ny] and check[nx][ny] == 0:
                    q.append((nx,ny))
                    check[nx][ny] = group_count
                    count += 1
    return count
n = int(input())
arr = [[] for _ in range(n)]
check = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count_result = []
group_count = 1
for i in range(n):
    value = input()
    for j in range(n):
        arr[i].append(int(value[j]))
for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and arr[i][j] != 0:
            count_result.append(bfs(i,j))
            group_count += 1
count_result = sorted(count_result)
print(len(count_result))
for i in count_result:
    print(i)