fibo_0 = [0] * 41
fibo_1 = [0] * 41
for i in range(0,41,1):
    if i == 0:
        fibo_0[i] = 1
        fibo_1[i] = 0
    elif i == 1:
        fibo_0[i] = 0
        fibo_1[i] = 1
    else:
        fibo_0[i] = fibo_0[i-1] + fibo_0[i-2]
        fibo_1[i] = fibo_1[i-1] + fibo_1[i-2]

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    print(fibo_0[n],fibo_1[n],sep=' ')