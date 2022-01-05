from collections import deque


def solution(bri_length, weight, truck):
    answer = 0
    deque_bri = deque(0 for i in range(bri_length))
    temp = 0

    while len(deque_bri):
        answer += 1
        temp = temp - deque_bri.popleft()
        if truck:
            temp = temp + truck[0]
            if weight >= temp:
                deque_bri.append(truck.pop(0))
            else:
                temp = temp - truck[0]
                deque_bri.append(0)
    return answer
#test1 = 2
#test2 = 10
#test3 = [7,4,5,6]

test1 = 100
test2 = 100
test3 = [10,10,10,10, 10,10,10,10,10,10]


print(solution(test1, test2, test3)) 
