def dfs(k,v):
    visited[v] = True
    for next_pos in arr[v]:
        if not (visited[next_pos]):
            dfs(k,next_pos)
            counted[k] += 1
    return counted[k]

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
counted = [0] * (n+1)
visited = [False] * (n+1)
max_value = -1
result = []
for _ in range(m):
    a,b = map(int,input().split())
    arr[b].append(a)
for i in range(1,n+1):
    c = dfs(i,i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
    visited = [False] * (n+1)
for e in result:
    print(e, end=" ")