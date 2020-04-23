def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(result[i],end=' ')
        print()
        return
    for i in range(start, len(arr)):
        result[depth] = arr[i]
        dfs(i+1, depth+1)
result = [0] * 13
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    dfs(0,0)
    print()