from itertools import combinations
while True:
    arr = list(input().split())
    if arr[0] == 0:
        break
    del arr[0]
    arr = list(combinations(arr,6))
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()
    print()