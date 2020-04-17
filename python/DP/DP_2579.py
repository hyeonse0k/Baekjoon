n = int(input())
value = [0] * n
max_value = [0] * n
for i in range(n):
    value[i] = int(input())

if n == 2:
    max_value[0] = value[0]
    max_value[1] = max(value[1], value[0] + value[1])
elif n == 1:
    max_value[0] = value[0]
else:
    max_value[0] = value[0]
    max_value[1] = max(value[1], value[0] + value[1])
    max_value[2] = max(value[0] + value[2], value[1] + value[2])

for i in range(3,n):
    max_value[i] = max(max_value[i-3] + value[i-1] + value[i], max_value[i-2] + value[i])
print(max_value[n-1])