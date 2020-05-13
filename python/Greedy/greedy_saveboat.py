from _collections import deque
def first_solution(people, limit):
    answer = 0
    people = sorted(people,reverse=True)
    dq = deque(people)
    print(dq)
    while dq:
        min_value = dq[-1]
        temp = dq.popleft()
        if not dq:
            answer += 1
            break
        if limit - temp >= min_value:
            temp += min_value
            dq.pop()
        answer += 1
    return answer
#list의 pop을 활용하였으나 pop은 list의 값을 뺀 후에 한 칸씩 앞으로 당기는 연산을 하기에,
#효율성 부분에서 실패하여 deque의 leftpop을 활용함으로써 문제를 해결하였다.
def solution(people,limit):
    people.sort()
    count = 0
    i ,j = 0, len(people)-1
    while i <= j:
        count += 1
        if people[j]+people[i] <= limit:
            i+=1
        j -= 1
    return count
#pop을 활용하지 않고 index를 활용하는 방법도 존재했다.
print(first_solution([70,80,50],100))