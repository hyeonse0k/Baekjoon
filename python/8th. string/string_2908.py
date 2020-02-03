num_list = list(map(int,input().split()))
for i in num_list:
    a = i // 100
    b = (i % 100)//10
    c = i % 10
    num_list[num_list.index(i)] = 100 * c + 10 * b + a
if num_list[0] > num_list[1]:
    print(num_list[0])
else:
    print(num_list[1])
