from collections import deque
v = deque()
v.append(1)
v.append(2)
print(len(v))
def solution(numbers):
    ans = ""
    temp = sorted(list(map(str,numbers)),reverse=True,key= lambda x: x*3)
    print(temp)
    for i in temp:
        ans += i
    if i.count('0') == len(i):
        ans = "0"
    return ans

numbers = [1200, 8, 7, 54]
print(solution(numbers))