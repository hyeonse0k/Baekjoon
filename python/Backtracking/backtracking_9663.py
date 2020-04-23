def check(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def dfs(n, current_row):
    if current_row == n:
        global count
        count += 1
        return

    for candidate_col in range(n):
        if check(current_candidate,candidate_col):
            current_candidate.append(candidate_col)
            dfs(n, current_row+1)
            current_candidate.pop() #backtrack하는 코드

n = int(input())
count = 0
current_candidate = []
dfs(n,0)
print(count)