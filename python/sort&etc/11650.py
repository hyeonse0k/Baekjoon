test_case = int(input())
array = []
for _ in range(test_case):
    input_data = input().split()
    array.append((int(input_data[0]),int(input_data[1])))

array = sorted(array)
for j in array:
    print(j[0],j[1])