n = int(input())
idx = 0
arr = [0] * 1001
while idx <= n:
    if idx <= 1:
        arr[idx] = 1
    else:
        arr[idx] = (arr[idx-1] + arr[idx-2]*2)%10007
    idx += 1
print(arr[n])