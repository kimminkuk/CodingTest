def solution(n, results):
    answer = 0
    winCase = [set() for i in range(n+1)]
    loseCase = [set() for i in range(n+1)]
    print(winCase, loseCase)
    for i in range(1, n+1):
        for result in results:
            if i == result[0]:
                winCase[i].add(result[1])
            if i == result[1]:
                loseCase[i].add(result[0])
        
        for loseList in winCase[i]:
            loseCase[loseList].update(loseCase[i])
        for winList in loseCase[i]:
            winCase[winList].update(winCase[i])

    print(winCase)
    print(loseCase)
    for i in range(1, n+1):
        if len(winCase[i]) + len(loseCase[i]) == n-1:
            answer = answer + 1
    return answer


test1 = 5
test2 = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(test1,test2))
