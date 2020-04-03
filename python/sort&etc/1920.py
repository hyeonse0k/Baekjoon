n = int(input())
string = map(int, input().split())
dic = {}
for i in string:
    dic.update({i: 0})

m = int(input())
ano_string = list(map(int, input().split()))
for i in ano_string:
    if i in dic:
        print(1)
    else:
        print(0)