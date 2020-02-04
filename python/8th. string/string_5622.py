def dial_num(num):
    if ord(num) >= ord('W'):
        return 10
    elif ord(num) >= ord('T'):
        return 9
    elif ord(num) >= ord('P'):
        return 8
    elif ord(num) >= ord('M'):
        return 7
    elif ord(num) >= ord('J'):
        return 6
    elif ord(num) >= ord('G'):
        return 5
    elif ord(num) >= ord('D'):
        return 4
    else:
        return 3
s = input()
sum = 0
for i in range(len(s)):
    sum += dial_num(s[i])
print(sum)