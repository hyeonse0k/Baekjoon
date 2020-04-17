def solve(k):
    if k == 1:
        arr[k] = 1
    elif k == 2:
        arr[k] = 2
    elif k == 3:
        arr[k] = 4
    else:
        arr[k] = solve(k-1) + solve(k-2) + solve(k-3)
    return arr[k]

test_case = int(input())
arr = [0] * 12
for _ in range(test_case):
    n = int(input())
    print(solve(n))