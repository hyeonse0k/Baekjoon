from itertools import combinations
n,c = map(int,input().split())
arr = sorted(list(map(str,input().split())))
vowel = ['a','e','i','o','u']
test = list(combinations(arr,n))
result = []
for i in test:
    count = 0
    for j in i:
        if j in vowel:
            count += 1
    if count >= 1 and count <= n-2:
        print(''.join(i))