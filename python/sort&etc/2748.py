fibo_num = [0 for i in range(91)]
fibo_num[0] = 0
fibo_num[1] = 1

a = int(input())
for i in range(2,a+1):
    fibo_num[i] = fibo_num[i-1] + fibo_num[i-2]
print(fibo_num[a])