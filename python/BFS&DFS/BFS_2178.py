from _collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        v = q.popleft()
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            for dx, dy in direction:
                nx, ny = v[0] + dx, v[1] + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if arr[nx][ny] and not visited[nx][ny] and check[nx][ny] == 0:
                    q.append((nx,ny))
                    check[nx][ny] = check[v[0]][v[1]] + 1

n,m = map(int,input().split())
arr = [[] for _ in range(n)]
check = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n):
    value = input()
    for j in range(m):
        arr[i].append(int(value[j]))
bfs(0,0)
print(check[n-1][m-1]+1)