test_case = int(input())
for _ in range(test_case):
    n,m = map(int,input().split())
    if n <= 11 or m <= 3:
        print(-1)
    else:
        print(m*11+4)