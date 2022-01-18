from collections import deque
def diff(a_, b_):
    cnt = 0
    a = a_
    b = b_
    for i in range(0, len(b)):
        if a[i] != b[i]:
            cnt = cnt + 1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    dq = deque([begin])
    check = False
    visited = []
    diffResult = False
    while dq:
        cnt = 0
        dqStep = dq.popleft()

        if dqStep == target:
            check = True
            break

        for i in words:
            diffResult = diff(dqStep, i) #True or False
            if diffResult == True and i not in visited:
                dq.append(i)
                visited.append(i)
                cnt = cnt + 1
                if cnt == 1:
                    answer = answer + 1

        if cnt == 0:
            answer = answer -1

    if check != True:
        answer = 0
    return answer

test1="hit"
test2="cog"
test3=["hot", "dot", "dog", "lot", "log"]
#test3=["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(test1,test2,test3))
