n = int(input())
arr = []
result = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr = sorted(arr, key=lambda x : (x[1],x[0]))
result.append(arr[0])
check = 0
for i in range(1,n):
    if arr[i][0] >= result[check][1]:
        result.append(arr[i])
        check += 1
print(len(result))