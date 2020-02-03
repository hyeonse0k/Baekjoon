a = int(input())
b = int(input())
c = int(input())
multiple = str(a*b*c)
num_list = list(0 for i in range(10))
for i in multiple:
    num_list[int(i)]+= 1
for i in range(10):
    print(num_list[i])