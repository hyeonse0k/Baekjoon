fibo = list(0 for i in range(46))
for i in range(46):
    if i <= 1:
        fibo[i] = i
    else:
        fibo[i] = fibo[i-1] + fibo[i-2]

num = int(input())
print(fibo[num])
