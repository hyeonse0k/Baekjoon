check = list(map(int, input().split(' ')))
ascending = True
descending = True
for i in range(1,8):
    if ascending:
        if check[i] > check[i-1]:
            descending = False
        elif check[i] < check[i-1]:
            ascending = False
if ascending:
    print("ascending")
elif descending:
    print("dexcending")
else:
    print("mixed")