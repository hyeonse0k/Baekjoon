n = int(input())
arr = []
max_w,count = 0,1
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr,reverse=True)
max_w = arr[0]
for i in range(1,n):
    count += 1
    if count * arr[i] > max_w:
        max_w = count * arr[i]
print(max_w)