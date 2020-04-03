test_count = int(input())
case = []
for _ in range(test_count):
    case.append(int(input()))
case.sort()
for i in case:
    print(i)