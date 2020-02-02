case_count = int(input())
for i in range(1,case_count+1):
    a, b = map(int, input().split())
    print('Case #{}: {}'.format(i,a+b))