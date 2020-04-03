n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

left = 1
right = 1
max_value = max(array)
now = array[0]
for i in range(1,n):
    if now < array[i]:
        left += 1
        now = array[i]

array.reverse()
now = array[0]
for i in range(1,n):
    if now < array[i]:
        right += 1
        now = array[i]
print(left,right,sep='\n')