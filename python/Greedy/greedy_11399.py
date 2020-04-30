n = int(input())
arr = list(map(int,input().split()))
ans = 0
arr = sorted(arr)
for i in range(n):
    for j in range(0,i+1):
        ans += arr[j]
print(ans)