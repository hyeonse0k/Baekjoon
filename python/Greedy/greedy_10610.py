n = list(input())
arr = []
for i in n:
    arr.append(int(i))
arr = sorted(arr,reverse=True)
test_sum = sum(arr[0:len(arr)-1])
if 0 not in arr or test_sum % 3 != 0:
    print(-1)
else:
    for i in range(len(n)):
        print(arr[i],end='')