n = int(input())
arr = [0] * 1000001
idx = 0
while idx <= n:
    if idx <= 1:
        arr[idx] = 0
        idx += 1
        continue
    if idx%3 == 0:
        arr[idx] = min(arr[idx//3]+1, arr[idx-1]+1)
    elif idx%2 == 0:
        arr[idx] = min(arr[idx//2]+1, arr[idx-1]+1)
    else:
        arr[idx] = arr[idx-1]+1
    idx += 1
print(arr[n])