n,m = map(int,input().split())
bundle_price = []
one_price = []
six_times_price = []
for i in range(m):
    a,b = map(int,input().split())
    bundle_price.append(a)
    one_price.append(b)
    six_times_price.append(b * 6)
min_one = min(one_price)
min_bundle = min(bundle_price)
min_six = min(six_times_price)
if n <= 6:
    print(min(min_one * n, min_bundle))
else:
    print(min(min_bundle,min_six) * (n//6) + min(min_one*(n%6),min_bundle))