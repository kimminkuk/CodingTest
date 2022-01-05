#case1
def solution(prices):
    answer = []
    pri_len = len(prices)
    for i in range (0, pri_len):
        cnt = 0
        for j in range(i+1, pri_len):
            cnt = cnt + 1  
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    return answer
test1 = [1,2,3,2,3]
print(solution(test1))
