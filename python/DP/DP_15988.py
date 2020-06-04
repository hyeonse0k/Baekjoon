test_case = int(input())
arr = [-1] * 10000001
arr[0] = 1
for _ in range(test_case):
    n = int(input())
    idx = 1
    while idx <= n:
        if arr[idx] != -1:
            idx += 1
            continue
        if idx <= 2:
            arr[idx] = idx
        else:
            arr[idx] = (arr[idx-3]+arr[idx-2]+arr[idx-1]) % 1000000009
        idx += 1
    print(arr[n])