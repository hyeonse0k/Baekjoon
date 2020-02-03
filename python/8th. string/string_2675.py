count = int(input())
for i in range(count):
    a,b = input().split()
    for j in range(len(b)):
        for k in range(int(a)):
            print(b[j],end ='')
    print()