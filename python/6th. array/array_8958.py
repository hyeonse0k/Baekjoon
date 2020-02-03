test_count = int(input())
for i in range(test_count):
    answer = list(input())
    score = 0
    continue_point = 0
    for j in answer:
        if j == 'O':
            if continue_point >= 1:
                continue_point += 1
                score += continue_point
            else:
                continue_point += 1
                score += 1
        else:
            continue_point = 0
    print(score)