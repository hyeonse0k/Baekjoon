case_count = int(input())
array = []
for i in enumerate(range(case_count)):
    age,name = input().split()
    t = (int(age),name,i[0])
    array.append(t)
array = sorted(array, key= lambda x: x[0])
for i in array:
    print(i[0],i[1])