import sys
test_case = int(input())
for _ in range(test_case):
    n = int(input())
    count = 1
    arr = []
    accept_value = []
    for _ in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))
    arr = sorted(arr, key= lambda x: x[0])
    min_value = arr[0][1]
    for i in range(1,n):
        if arr[i][1] < min_value:
            count += 1
            accept_value.append(arr[i][1])
            min_value = min(accept_value)
    print(count)