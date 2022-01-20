from collections import deque
def solution(n, vex):
    answer = 0
    adj= [[] for i in range(n+1)]
    temp = [ -1 for i in range(n+1)]
    for i in vex:
        x = i[0]
        y = i[1]
        adj[x].append(y)
        adj[y].append(x)
    #print(adj)
    dq = deque([[1,0]]) #v, cnt
    visited = []
    cnt = 0
    
    while dq:
        node = dq.popleft()
        if temp[node[0]] == -1: #-1..
            temp[node[0]] = node[1]
            cnt = node[1] + 1
            for i in adj[node[0]]:
                #if i not in visited:
                dq.append([i,cnt])
    #print(temp)
    tt = max(temp)
    for i in temp:
        if i == tt:
            answer = answer + 1
    return answer
