import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        if scoville[0] >= K:
            break
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        mixSo = s1 + s2*2
        heapq.heappush(scoville,mixSo)
        answer = answer + 1

    if scoville[0] < K:
        answer = -1
    
    return answer

#test1= [1,2,3,9,10,12]
#test2 = 7

#test1= [1,2,3,4,5,6]
#test2 = 100

test1 = [50,40,1000,20,700]
test2 = 5

print(solution(test1,test2))
