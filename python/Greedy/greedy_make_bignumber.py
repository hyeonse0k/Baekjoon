from itertools import combinations
def first_solution(number, k):
    answer = ''
    number = list(map(int,number))
    combi = list(combinations(number ,len(number) - k))
    res = []
    for i in range(len(combi)):
        sum_value = 0
        k = 0
        for j in range(len(combi[0])-1,-1,-1):
            sum_value += combi[i][k] * (10 ** j)
            k += 1
        res.append(sum_value)
    answer = str(max(res))
    return answer
#파이썬 내장 itertools의 combinations를 활용하여 문제를 풀고자 하였으나
#문제에서 입력 가능한 문자열의 자릿수가 최대 100만 자리인 점을 간과하여 풀었기에 시간초과 발생

def second_solution(number,k):
    number = list(number)
    combi = list(combinations(number,len(number)-k))
    idx = 0
    while len(combi) > 1:
        new_combi = []
        combi = sorted(combi, key=lambda x: x[idx],reverse=True)
        max_value = combi[0][idx]
        for i in combi:
            if i[idx] == max_value:
                new_combi.append(i)
            else:
                break
        if combi == new_combi:
            break
        combi = new_combi
        idx += 1
    answer = "".join(combi[0])
    return  answer
#combinations가 문제인줄 모르고 계속 방법을 바꿔가며 최적화를 시도하였으나
#근본적인 접근 방법이 잘못되었기에 시간 초과가 계속 발생

def solution(number,k):
    number = list(number)
    arr = []
    for i in range(len(number)):
        while len(arr) > 0 and k > 0 and int(number[i]) > int(arr[-1]):
            arr.pop()
            k -= 1
        if k == 0:
            arr += number[i:]
            break
        arr.append(number[i])
    if k > 0:
        arr = arr[:-k]
    return "".join(arr)
#접근방식을 바꾸어 정렬 없이 앞 자리에서 부터 가장 큰 수를 채워나간다는 근본적인 접근방법으로 문제를 해결하였다.

print(solution("124",1))