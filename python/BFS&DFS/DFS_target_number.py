def dfs(numbers, target, index, sum):
    if index == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    else:
        return dfs(numbers,target, index+1,sum+numbers[index]) + dfs(numbers,target,index+1, sum-numbers[index])

def solution(numbers, target):
    return dfs(numbers,target,0,0)

print(solution([1, 1, 1, 1, 1],3))

