string = input()
temp_str = ""
result = 0
chk_minus = False
for i in range(len(string)+1):
    if i == len(string): #문자열이 끝난 경우
        if chk_minus:
            result -= int(temp_str)
        else:
            result += int(temp_str)
        continue

    if string[i] == '+' or string[i] == '-':
        if chk_minus:
            result -= int(temp_str)
        else:
            result += int(temp_str)
        temp_str = ""

        if string[i] == '-':
            chk_minus = True
    else:
        temp_str += string[i]
print(result)