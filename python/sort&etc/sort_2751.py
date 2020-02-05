def quicksort(arr):
    if len(arr) <= 1:
        return arr
    left, right = list(), list()
    pivot = arr[0]
    for i in range(1, len(arr)):
        if pivot > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)
'''
Big O(nlogn)을 갖는 quick sort를 이용해 정렬하려 했으나,
quick sort는 최악의 경우 n^2의 시간복잡도를 가지므로 "시간초과" 되어
성공하지 못하였다.
'''
count = int(input())
num_arr = list(0 for i in range(count))
for i in range(count):
    num_arr[i] = int(input())
sort_list = quicksort(num_arr)
for i in range(len(num_arr)):
    print(num_arr[int(i)])