import math
def solution(progresses, speeds):
    answer = []
    dueStk = []
    tt = 0
    pro_len = len(progresses)
    for i in range(0, pro_len):
        #dueStk.append( (100-progresses[i]) / speeds[i])
        #dueStk.insert(0, (100-progresses[i]) / speeds[i])
        #dueStk.insert(0, int((100-progresses[i]) / speeds[i]) + 1)
        dueStk.insert(0, math.ceil((100-progresses[i]) / speeds[i]))
    #print(dueStk)
    temp = dueStk[-1] #7
    while dueStk:
        if dueStk[-1] <= temp:
            dueStk.pop()
            tt += 1
        else:
            answer.append(tt)
            temp = dueStk[-1]
            tt = 0
    if tt != 0:
        answer.append(tt)
    return answer


#test1 = [93, 30, 55]
#test1 = [95, 90, 99, 99, 80, 99]
test1 = [99,98,97,96]
test2 = [4,3,4,6]
#test2 = [1, 30, 5]
#test2 = [1, 1, 1, 1, 1, 1]


print(solution(test1, test2))
