n = int(input())
dp = [0] * n
arr = list(map(int,input().split()))

for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    else:
        dp[i] = max(dp[i-1] + arr[i], arr[i])
print(max(dp))