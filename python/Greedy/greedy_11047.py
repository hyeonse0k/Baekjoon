n,k = map(int,input().split())
coin = []
now_sum, sum ,count = 0,0,0
for _ in range(n):
    coin.append(int(input()))
while sum < k:
    for i in range(n-1,-1,-1):
        now_sum += coin[i]
        if now_sum > k:
            now_sum = sum
        else:
            sum = now_sum
            count += 1
            break
print(count)