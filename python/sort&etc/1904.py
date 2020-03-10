fibo_num = [0 for i in range(1000001)]
fibo_num[0] = 1
fibo_num[1] = 2
a = int(input())
for i in range(2,a+1):
    fibo_num[i] = (fibo_num[i-1] + fibo_num[i-2]) % 15746

print(fibo_num[a-1])
