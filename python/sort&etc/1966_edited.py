test_case = int(input())
for _ in range(test_case):
    n,m = map(int, input().split())
    arr = list(map(int,input().split()))
    arr = [(i, idx) for idx, i in enumerate(arr)]
    result = list()
    while len(arr) >= 1:
        n = 0
        while n <= len(arr):
            if arr[0][0] != max(arr)[0]:
                arr.append(arr.pop(0))
            else:
                result.append(arr.pop(0))
                n += 1
    for i in range(len(result)):
       if result[i][1] == m:
            print(i+1)