from _collections import deque
def bfs(n,m):
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    day = -1
    while tomato:
        day += 1
        for _ in range(len(tomato)):
            v = tomato.popleft()
            for dx, dy in direction:
                nx, ny = v[0]+dx, v[1]+dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[v[0]][v[1]] + 1
                    tomato.append((nx,ny))
    for i in arr:
        if 0 in i:
            return -1
    return day

n,m = map(int,input().split())
arr = [[] for _ in range(m)]
tomato = deque()
for i in range(m):
    value = list(input().split())
    for j in range(n):
        arr[i].append(int(value[j]))
        if int(value[j]) == 1:
            tomato.append((i,j))
print(bfs(n,m))