count = int(input())
num_arr = list(0 for i in range(count))
for i in range(count):
    num_arr[int(i)] = int(input())
for i in range(len(num_arr)-1):
    swap = False
    for j in range(len(num_arr) - i - 1):
        if num_arr[j] > num_arr[j+1]:
            num_arr[j],num_arr[j+1] = num_arr[j+1], num_arr[j]
            swap = True
    if swap == False:
            break
for k in range(len(num_arr)):
    print(num_arr[int(k)])