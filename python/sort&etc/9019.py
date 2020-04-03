import queue
MAX = 10000
def bfs(a,b):
    visited = list(False for i in range(10001))
    data = queue.Queue()
    data.put((a,""))
    visited[a] = True
    while not data.empty():
        num, change = data.get()
        if num == b:
            return change

        calNum = (2 * num) % MAX
        if not visited[calNum]:
            visited[calNum] = True
            data.put((calNum, change+"D"))

        if num -1 == -1:
            calNum = 9999
        else:
            calNum = num -1
        if not visited[calNum]:
            visited[calNum] = True
            data.put((calNum, change+"S"))

        calNum = (num % 1000) * 10 + num // 1000
        if not visited[calNum]:
            visited[calNum] = True
            data.put((calNum, change + "L"))

        calNum = (num % 10) * 1000 + (num // 10)
        if not visited[calNum]:
            visited[calNum] = True
            data.put((calNum, change + "R"))


test_case = int(input())
for _ in range(test_case):
    a, b = map(int, input().split())
    print(bfs(a,b))
