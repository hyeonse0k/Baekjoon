s = input()
alphabet = list(-1 for i in range(26))
for i in range(len(s)):
    if alphabet[ord(s[i])-ord("a")] == -1:
        alphabet[ord(s[i])-ord('a')] = i
for j in alphabet:
    print(j, end=' ')