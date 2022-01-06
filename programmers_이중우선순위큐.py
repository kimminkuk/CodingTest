import heapq
def solution(operations):
    answer = []
    oper_max = []
    oper_min = []

    check = 0
    for i in operations:
        tt = i.split()
        if tt[0] == 'I':
            ttt = int(tt[1])
            heapq.heappush(oper_max, (-ttt, ttt))
            heapq.heappush(oper_min, ttt)
            #check = check + 1
        else:
            if len(oper_max) == 0 or len(oper_min) == 0:
                pass
            else:
                if tt[1] == '1':
                    temp = heapq.heappop(oper_max)[1]
                    oper_min.remove(temp)
                else:
                    temp = heapq.heappop(oper_min)
                    oper_max.remove((temp * -1, temp))

    if oper_max and oper_min:
        answer.append( heapq.heappop(oper_max)[1] )
        answer.append(heapq.heappop(oper_min))
    else:
        answer = [0,0]
    return answer
  
  #test1 = ["I 16", "D 1"]
#test1 = ["I 7", "I 5", "I -5", "D -1"]
#test1 = ["I 50", "I 10", "I 20"]
#test1 =["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
test1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(test1)) 
