s = list(input())
alphabet = list(0 for i in range(26))
for i in range(len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        alphabet[ord(s[i])-ord('A')] += 1
    else:
        alphabet[ord(s[i])-ord('a')] += 1
max = 0
max_index = 0
max_count = 0
for j in range(26):
    if alphabet[j] >= max:
        if alphabet[j] == max:
            max_count += 1
        else:
            max = alphabet[j]
            max_count = 0
            max_index = j
if max_count >= 1:
    print('?')
else:
    print(chr(max_index+ord('A')))