array = input()
find_word = input()

index = 0
result = 0
while len(array) - index >= len(find_word):
    if array[index: index + len(find_word)] == find_word:
        result += 1
        index += len(find_word)
    else:
        index += 1
print(result)